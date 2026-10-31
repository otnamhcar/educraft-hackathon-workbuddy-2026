#!/usr/bin/env python3
"""Install the four EduCraft skills where WorkBuddy looks for them.

One implementation, three operating systems. Nothing is compiled and no package
manager is involved: a skill is a folder containing SKILL.md, and "installing"
it means copying that folder into the directory the agent reads at session start.

    Linux / macOS      python3 tools/install_skills.py
    Windows (cmd)      python tools\\install_skills.py
    Windows (py)       py tools\\install_skills.py

Destination, first match wins:

    1. --dest <path>
    2. the WORKBUDDY_SKILLS_DIR environment variable
    3. ~/.workbuddy-ai/skills          (on Windows: C:\\Users\\<you>\\.workbuddy-ai\\skills)

Why Python and not bash: the team is split across Linux and Windows, and a bash
script silently becomes a different program under Git Bash, WSL and cmd. This
file behaves the same everywhere, including the error messages.

Exit codes: 0 = installed and verified, 1 = verification failed, 2 = bad input.
"""

import argparse
import os
import shutil
import sys
from pathlib import Path

SKILLS = ("edu-orchestrator", "edu-planner", "edu-writer", "edu-reviewer")
REPO_ROOT = Path(__file__).resolve().parent.parent
SRC = REPO_ROOT / "05_Bukti_Proses" / "skills_package"


def resolve_dest(cli_value):
    """Where the skills go. Never guesses silently — the resolved path is printed."""
    if cli_value:
        return Path(cli_value).expanduser().resolve()
    env = os.environ.get("WORKBUDDY_SKILLS_DIR")
    if env:
        return Path(env).expanduser().resolve()
    # Path.home() works with HOME unset on POSIX (pwd fallback) and with USERPROFILE
    # on Windows, which is why this no longer crashes in a bare shell.
    return Path.home() / ".workbuddy-ai" / "skills"


def fail(message, code=2):
    print("ERROR: " + message, file=sys.stderr)
    return code


def harden_console():
    """Do not crash on a path the console cannot encode (Windows cp1252)."""
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(errors="replace")
        except (AttributeError, ValueError):
            pass


def replace_tree(src, target):
    """Make target a fresh copy of src, removing any previous install first.

    On Windows an editor, antivirus or the agent itself can hold a file open, and
    the delete fails with PermissionError. That is a normal thing to hit on a
    laptop, so it gets a readable message instead of a traceback.
    """
    if target.is_symlink() or target.is_file():
        target.unlink()
    elif target.is_dir():
        shutil.rmtree(target)
    shutil.copytree(src, target)


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Copy the four EduCraft skills into the WorkBuddy skills directory."
    )
    parser.add_argument(
        "--dest",
        help="destination directory (overrides WORKBUDDY_SKILLS_DIR and the default)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="show what would be copied, change nothing",
    )
    args = parser.parse_args(argv)

    harden_console()

    if not SRC.is_dir():
        return fail(
            "{} not found. Are you running this from a full clone of the "
            "repository?".format(SRC)
        )

    missing = [s for s in SKILLS if not (SRC / s / "SKILL.md").is_file()]
    if missing:
        return fail(
            "these skill folders have no SKILL.md: {}. The clone is incomplete.".format(
                ", ".join(missing)
            )
        )

    dest = resolve_dest(args.dest)
    print("Source : {}".format(SRC))
    print("Target : {}".format(dest))
    print("")

    if args.dry_run:
        for s in SKILLS:
            print("  would install  {}".format(s))
        print("\nDry run: nothing was written.")
        return 0

    try:
        dest.mkdir(parents=True, exist_ok=True)
    except OSError as exc:
        return fail("cannot create {}: {}".format(dest, exc))

    for s in SKILLS:
        target = dest / s
        # Only ever touch a folder we own: the name comes from the fixed SKILLS
        # tuple above, never from user input or a glob.
        try:
            replace_tree(SRC / s, target)
        except OSError as exc:
            return fail(
                "could not replace {}: {}\n"
                "       If a file is open in an editor or the agent is running, close it "
                "and retry.".format(target, exc)
            )
        print("  installed  {}".format(s))

    found = sorted(p.name for p in dest.iterdir() if p.is_dir() and p.name.startswith("edu-"))
    print("\nSkills now present: {} (expected 4)".format(len(found)))

    if len(found) != 4:
        print(
            "ERROR: expected 4 edu-* folders in {}, found {}: {}".format(
                dest, len(found), ", ".join(found) or "none"
            ),
            file=sys.stderr,
        )
        return 1

    print(
        """
Done. Two things before it works:
  1. RESTART WorkBuddy -- the skill list is read when a session opens.
  2. Confirm in a new chat that `edu-orchestrator` is recognised.

Then check the rest of the clone:
  python3 tools/doctor.py        (Windows: python tools\\doctor.py)"""
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
