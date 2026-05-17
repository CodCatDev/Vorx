import vorx.scene
import ctypes
import vorx.core.window
from pathlib import Path
from json import loads
try:
    configDir = Path(__file__).resolve().parent / ".vorx" / "config.json"
    config = loads(open(configDir, 'r', encoding="utf-8").read())
except:
    print("VorxError: No configuration file found. Run 'vorx init' to create one.")
    exit(1)
sceneDir = Path(__file__).resolve().parent / "scenes"
scenes = {}
for scene, file in config['data']['scenes'].items():
    scenes[scene] = vorx.scene.RawScene(open(sceneDir / (file + ".vxs"), 'r', encoding="utf-8"), file)
window = vorx.core.window.Window()
sdl = window.getSdl()
ext = window.getExt()
running = True
event = sdl.SDL_Event()
try:
    currentScene = scenes[config['defaultScene']]
except:
    print("VorxError: No default scene found. Run 'vorx init' to create one.")
    exit(1)
while running:
    while sdl.SDL_PollEvent(ctypes.byref(event)) != 0:
        if event.type == sdl.SDL_QUIT:
            running = False
    window.draw(currentScene)