import json

class SpriteManager():

    def __init__(self):
        with open("./sprites.json", "r", encoding="utf-8") as f:
            self.sheet = json.load(f)

    
    def get_egg_sprites(self):
        return self.sheet["egg"]
