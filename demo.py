from vorx.core.window import Window
from vorx.objects.shapes import Rect, Polygon

def main():
    win = Window()
    win.window.show()

    red_rect = Rect(50.0, 50.0, 200.0, 150.0, 255, 0, 0)
    green_rect = Rect(370.0, 400.0, 100.0, 100.0, 0, 255, 0)
    
    blue_tri = Polygon([
        (600.0, 100.0),
        (750.0, 300.0),
        (450.0, 300.0)
    ], 0, 0, 255)

    yellow_penta = Polygon([
        (600.0, 350.0),
        (680.0, 410.0),
        (650.0, 500.0),
        (550.0, 500.0),
        (520.0, 410.0)
    ], 255, 255, 0)

    random_poly = Polygon([
        (100.0, 300.0),
        (250.0, 350.0),
        (200.0, 450.0),
        (350.0, 400.0),
        (300.0, 550.0),
        (150.0, 500.0),
        (50.0, 550.0),
        (80.0, 400.0)
    ], 255, 0, 255)

    scene = [red_rect, green_rect, blue_tri, yellow_penta, random_poly]

    ext = win.getExt()
    sdl = win.getSdl()

    running = True
    while running:
        for event in ext.get_events():
            if event.type == sdl.SDL_QUIT:
                running = False
                break
        
        win.draw(scene)

    ext.quit()

if __name__ == "__main__":
    main()
