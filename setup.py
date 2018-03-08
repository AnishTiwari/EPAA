import sys
from cx_Freeze import setup, Executable

setup(
    name = "Test analysis",
    version = "1.0",
    description = "Analysis for internal test marks",
    executables = [Executable("test.py", base = "Win32GUI")])