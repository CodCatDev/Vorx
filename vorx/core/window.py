import os
from pathlib import Path
import sys
import platform
import ctypes
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
from .renderer import buildGeometryBatch, freeGeometryBatch

class Window:
    def __init__(self):
        ext.init()
        self.window = ext.Window("Vorx", size=(800, 600))
        self.renderer = ext.Renderer(self.window)

    def draw(self, scene_shapes):
        self.renderer.clear()
        
        v_addr, i_addr, num_v, num_i = buildGeometryBatch(scene_shapes)
        
        if num_v > 0:
            c_vertices = ctypes.cast(v_addr, ctypes.POINTER(sdl2.SDL_Vertex))
            c_indices = ctypes.cast(i_addr, ctypes.POINTER(ctypes.c_int))
            
            sdl2.SDL_RenderGeometry(
                self.renderer.sdlrenderer,
                None,
                c_vertices, num_v,
                c_indices, num_i
            )
            
            freeGeometryBatch(v_addr, i_addr)
            
        self.renderer.present()

    def getExt(self):
        return ext

    def getSdl(self):
        return sdl2
