import vorx.scene

scene = vorx.scene.RawScene(open("myScene.vxs", 'r', encoding="utf-8"), "myScene.vsx")

import vorx.core.window

window = vorx.core.window.Window()

import ctypes

sdl = window.getSdl()
ext = window.getExt()

running = True
event = sdl.SDL_Event()

while running:
    while sdl.SDL_PollEvent(ctypes.byref(event)) != 0:
        if event.type == sdl.SDL_QUIT:
            running = False

    window.draw(scene)
