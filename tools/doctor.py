#!/usr/bin/env python3
"""Is this clone healthy enough to run?

Six checks, one implementation for Linux, macOS and Windows. Exit 0 only if all
pass. Every check states what it looked at, so a failure says *where* to look
rather than just that something is wrong.

    Linux / macOS      python3 tools/doctor.py
    Windows (cmd)      python tools\\doctor.py
    Windows (py)       py tools\\doctor.py

Options:
    --dest <path>   where the skills were installed (same resolution as
                    install_skills.py: flag, then WORKBUDDY_SKILLS_DIR, then
                    ~/.workbuddy-ai/skills)
    --no-color      plain text, also honoured via the NO_COLOR environment variable

Exit codes: 0 = ready, 1 = at least one check failed, 2 = cannot start.
"""

import argparse
import hashlib
import os
import subprocess
import sys
import tempfile
from pathlib import Path

SKILLS = ("edu-orchestrator", "edu-planner", "edu-writer", "edu-reviewer")
REPO_ROOT = Path(__file__).resolve().parent.parent
PKG = REPO_ROOT / "05_Bukti_Proses" / "skills_package"
KNOWLEDGE = REPO_ROOT / "03_Hasil" / "referensi"
CHECKER = REPO_ROOT / "tools" / "check_grounding.py"

KNOWLEDGE_FILES = (
    "rulebook_ipas.md",
    "cp_ipas.md",
    "konteks_aktual.md",
    "source_material_energi.md",
    "source_material_wujud_zat.md",
)

# Files that exist in several places and must stay byte-identical. Drift here is
# the quiet failure: the Reviewer would judge against rules the Writer never saw.
COPY_GROUPS = ("rulebook_ipas.md", "source_material_wujud_zat.md")

RUNS = ("03_Hasil/materi_ajar", "03_Hasil/edu_output_wujud_zat")


# --------------------------------------------------------------------------- #
# Output. Windows consoles do not do ANSI by default, and a failed colour escape
# is a confusing way to learn that. Enable VT mode where possible, else plain.
# --------------------------------------------------------------------------- #

class Reporter(object):
    def __init__(self, color):
        self.color = color
        self.passed = 0
        self.failed = 0
        self.warned = 0

    def _paint(self, text, code):
        if not self.color:
            return text
        return "\033[{}m{}\033[0m".format(code, text)

    def heading(self, text):
        print("\n" + text)

    def ok(self, text):
        self.passed += 1
        print("  {}  {}".format(self._paint("PASS", "32"), text))

    def no(self, text):
        self.failed += 1
        print("  {}  {}".format(self._paint("FAIL", "31"), text))

    def warn(self, text):
        self.warned += 1
        print("  {}  {}".format(self._paint("WARN", "33"), text))


def _enable_windows_vt():
    """Turn on ANSI escape processing in the Windows console. Best effort."""
    try:
        import ctypes

        kernel32 = ctypes.windll.kernel32
        handle = kernel32.GetStdHandle(-11)  # STD_OUTPUT_HANDLE
        mode = ctypes.c_uint32()
        if not kernel32.GetConsoleMode(handle, ctypes.byref(mode)):
            return False
        return bool(kernel32.SetConsoleMode(handle, mode.value | 0x0004))
    except Exception:
        return False


def _harden_console():
    """Never crash on a path a console cannot encode.

    A Windows console is often cp1252, and a user name or folder outside that
    range would raise UnicodeEncodeError while printing a *diagnostic* -- the one
    moment the message matters most.
    """
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(errors="replace")
        except (AttributeError, ValueError):
            pass  # Python 3.6, or a stream that is not a TextIOWrapper


def use_color(requested_off, stream):
    if requested_off or os.environ.get("NO_COLOR"):
        return False
    try:
        if not stream.isatty():
            return False
    except Exception:
        return False
    if os.name == "nt":
        return _enable_windows_vt()
    return True


# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #

def resolve_dest(cli_value):
    if cli_value:
        return Path(cli_value).expanduser().resolve()
    env = os.environ.get("WORKBUDDY_SKILLS_DIR")
    if env:
        return Path(env).expanduser().resolve()
    return Path.home() / ".workbuddy-ai" / "skills"


def sha256(path):
    digest = hashlib.sha256()
    with open(str(path), "rb") as handle:
        for block in iter(lambda: handle.read(65536), b""):
            digest.update(block)
    return digest.hexdigest()


def first_line(text):
    for line in text.splitlines():
        if line.strip():
            return line.strip()
    return "(no output)"


# --------------------------------------------------------------------------- #
# Checks
# --------------------------------------------------------------------------- #

def check_python(rep):
    rep.heading("1. Python")
    version = "{}.{}".format(sys.version_info[0], sys.version_info[1])
    if sys.version_info < (3, 6):
        rep.no("Python {} -- 3.6 or newer is required".format(version))
        return
    rep.ok("python {} ({})".format(version, sys.executable))


def check_contracts(rep):
    rep.heading("2. Skill contracts present in the clone")
    missing = [s for s in SKILLS if not (PKG / s / "SKILL.md").is_file()]
    if missing:
        for s in missing:
            rep.no("missing {}".format(PKG / s / "SKILL.md"))
        return
    rep.ok("4 of 4 contracts found")


def check_installed(rep, dest):
    rep.heading("3. Skills installed for WorkBuddy")
    if not dest.is_dir():
        rep.no("{} does not exist -- run install_skills.py".format(dest))
        return
    found = sorted(p.name for p in dest.iterdir() if p.is_dir() and p.name.startswith("edu-"))
    if len(found) == 4:
        rep.ok("4 edu-* skills installed in {}".format(dest))
    else:
        rep.no(
            "{} of 4 installed in {} -- run install_skills.py, then restart "
            "WorkBuddy".format(len(found), dest)
        )


def check_knowledge(rep):
    rep.heading("4. Knowledge layer")
    missing = [name for name in KNOWLEDGE_FILES if not (KNOWLEDGE / name).is_file()]
    if missing:
        for name in missing:
            rep.no("missing {}".format(KNOWLEDGE / name))
        return
    rep.ok("rulebook, CP, actual-context register and both source sheets found")


def check_copies(rep):
    rep.heading("5. Copies identical (rulebook, wujud-zat source)")
    for name in COPY_GROUPS:
        canonical = KNOWLEDGE / name
        if not canonical.is_file():
            rep.no("{} -- canonical copy missing".format(name))
            continue
        copies = [canonical]
        for skill in SKILLS:
            candidate = PKG / skill / "assets" / name
            if candidate.is_file():
                copies.append(candidate)
        if len(copies) < 2:
            rep.no("{} -- only one copy, nothing to compare".format(name))
            continue
        sums = {sha256(p) for p in copies}
        if len(sums) == 1:
            rep.ok(
                "{} -- one checksum across {} copies ({})".format(
                    name, len(copies), sha256(canonical)[:16]
                )
            )
        else:
            rep.no(
                "{} -- {} distinct checksums across {} copies, they have "
                "drifted".format(name, len(sums), len(copies))
            )


def check_grounding(rep):
    rep.heading("6. Grounding check (R001)")
    if not CHECKER.is_file():
        rep.no("{} not found".format(CHECKER))
        return

    tempdir = tempfile.mkdtemp(prefix="educraft-doctor-")
    try:
        for run in RUNS:
            report = os.path.join(tempdir, "grounding.md")
            command = [
                sys.executable,
                str(CHECKER),
                "--run",
                run,
                "--knowledge",
                str(KNOWLEDGE.relative_to(REPO_ROOT)),
                "--out",
                report,
            ]
            try:
                result = subprocess.run(
                    command,
                    cwd=str(REPO_ROOT),
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    universal_newlines=True,
                )
            except OSError as exc:
                rep.no("{} -- could not start the checker: {}".format(run, exc))
                continue
            line = first_line(result.stdout or "")
            if result.returncode == 0:
                rep.ok("{} -- {}".format(run, line))
            else:
                rep.no("{} -- {}".format(run, line))
    finally:
        try:
            for name in os.listdir(tempdir):
                os.remove(os.path.join(tempdir, name))
            os.rmdir(tempdir)
        except OSError:
            pass  # a leftover temp file is not worth failing the run over


# --------------------------------------------------------------------------- #

def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Check whether this clone is ready to run."
    )
    parser.add_argument("--dest", help="where the skills were installed")
    parser.add_argument("--no-color", action="store_true", help="plain text output")
    args = parser.parse_args(argv)

    _harden_console()

    if not (REPO_ROOT / "03_Hasil").is_dir():
        print(
            "ERROR: {} does not look like the repository root. Run this script "
            "from inside a clone.".format(REPO_ROOT),
            file=sys.stderr,
        )
        return 2

    rep = Reporter(use_color(args.no_color, sys.stdout))
    dest = resolve_dest(args.dest)

    print("Repository: {}".format(REPO_ROOT))
    print("Skills dir: {}".format(dest))

    check_python(rep)
    check_contracts(rep)
    check_installed(rep, dest)
    check_knowledge(rep)
    check_copies(rep)
    check_grounding(rep)

    print("\n" + "-" * 32)
    print("  {} passed / {} failed / {} warning".format(rep.passed, rep.failed, rep.warned))
    print("-" * 32)

    if rep.failed > 0:
        print("  Not ready. Fix the FAIL lines above.")
        return 1
    print('  Ready. Start with: README.md -> "Run it yourself"')
    return 0


if __name__ == "__main__":
    sys.exit(main())
