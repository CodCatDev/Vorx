import os
from pathlib import Path
import sys
import platform
import ctypes
from ..conf import VERSION, BUILD

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

def hexToRgb(hex_code):
    hex_code = hex_code.lstrip('#')
    return tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))

os.environ['PYSDL2_DLL_PATH'] = str(libDir)
import sdl2
import sdl2.ext as ext
from .renderer import renderScene

class Window:
    def __init__(self):
        ext.init()
        self.window = ext.Window("Vorx", size=(800, 600), flags=sdl2.SDL_WINDOW_RESIZABLE)
        self.renderer = ext.Renderer(self.window, flags=sdl2.SDL_RENDERER_ACCELERATED)
        info = sdl2.SDL_RendererInfo()
        sdl2.SDL_GetRendererInfo(self.renderer.sdlrenderer, ctypes.byref(info))
        print(f"Vorx Engine {VERSION}-{BUILD} (Graphics: {info.name.decode()}, run on {platform.system()} {platform.release()})")

        self.rawRendererPtr = ctypes.cast(self.renderer.sdlrenderer, ctypes.c_void_p).value
        
        self.cVertices = None
        self.cIndices = None

    def draw(self, rawScene):

        scene = rawScene.parse

        r, g, b = hexToRgb(scene['background'])

        self.renderer.clear(color=[r, g, b, 255])
        
        renderScene(self.rawRendererPtr, scene['objects'])
        
        self.renderer.present()

    def getExt(self):
        return ext

    def getSdl(self):
        return sdl2
