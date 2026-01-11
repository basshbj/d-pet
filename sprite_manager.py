import json
from tools.utils import customJsonDecoder

class SpriteManager():

    def __init__(self):
        with open("./sprites.json", "r", encoding="utf-8") as f:
            self.sheet = json.loads(f.read(), object_hook=customJsonDecoder)

    
    def get_egg_sprites(self):
        return self.sheet.stages[0].sprites
