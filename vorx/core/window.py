import os
from pathlib import Path
import sys
import platform
libsDir = Path(__file__).resolve().parent.parent.parent / "lib"
runningOS = os.name

if sys.platform == "win32":
    libDir = libsDir / "win"
elif sys.platform == "linux":
    libDir = libsDir / "linux"
elif sys.platform == "darwin":
    arch = platform.machine().lower()
    if arch in ("arm64", "aarch64"):
        libDir = libsDir / "macos-m"
    else:
        libDir = libsDir / "macos-in"
os.environ['PYSDL2_DLL_PATH'] = str(libDir)
import sdl2
import sdl2.ext as ext

