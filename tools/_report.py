"""Shared console output for the EduCraft tools.

Two scripts report check results (``doctor.py``, ``check_capture.py``) and both
have to survive the same hostile console: a Windows cmd window at cp1252, a
redirect into a file, a CI log with no terminal attached. Duplicating that logic
would mean fixing the same bug twice, so it lives here.

ASCII only. Colour is opt-in and degrades to plain text.
"""

import os
import sys


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

    def plain(self, text):
        """Neutral line: context, not a verdict. Does not affect the counts."""
        print(text)

    def ok(self, text):
        self.passed += 1
        print("  {}  {}".format(self._paint("PASS", "32"), text))

    def no(self, text):
        self.failed += 1
        print("  {}  {}".format(self._paint("FAIL", "31"), text))

    def warn(self, text):
        self.warned += 1
        print("  {}  {}".format(self._paint("WARN", "33"), text))

    def summary(self):
        print("\n" + "-" * 32)
        print("  {} passed / {} failed / {} warning".format(
            self.passed, self.failed, self.warned))
        print("-" * 32)


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


def harden_console():
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
