import json
from io import TextIOWrapper
from .parser import sceneParser

class RawScene:
    def __init__(self, file: TextIOWrapper, fileName: str):
        self.file = file
        try:
            self.data = json.load(file)
        except Exception as e:
            print(f"VorxError: Invalid scene '{fileName}' data. Maybe, the file is corrupted?")
            print(f"Detail error: '{e}'")
            exit(1)
        
        self.parse = sceneParser(self.data)
    
    def __repr__(self) -> str:
        return f"vorx.scene.RawScene(fileName='{self.file.name}', file=TextIOWrapper(...))"

