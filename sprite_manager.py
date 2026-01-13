import json
from tools.utils import customJsonDecoder, StageLevel

class SpriteManager():

    def __init__(self):
        with open("./sprites.json", "r", encoding="utf-8") as f:
            self.sheet = json.loads(f.read(), object_hook=customJsonDecoder)

    
    def get_sprites(self, level: StageLevel):
        return self.sheet.stages[level.value].sprites