from ..objects.shapes import Rect

def sceneParser(scene: dict):
    parsedScene = {
        "name": scene.get("name", "MyScene"),
        "background": scene.get("background", "#000000"),
        "objects": []
    }

    for obj in scene.get("objects", []):
        obj_type = obj.get("type")
        
        if obj_type == "rect":
            r, g, b = obj.get("color", [255, 255, 255])
            
            parsedScene["objects"].append(
                Rect(obj.get("x", 0), obj.get("y", 0), obj.get("w", 10), obj.get("h", 10), r, g, b)
            )

    return parsedScene