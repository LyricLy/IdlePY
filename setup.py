import sys
from cx_Freeze import setup, Executable

setup(
    name = "IdlePY",
    version = "0.2",
    description = "An idle game that works in the command line/terminal created in Python.",
    executables = [Executable("IdlePY.py", base = "Win32GUI")])