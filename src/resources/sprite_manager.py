import json
from utils.utils import customJsonDecoder, StageLevel


class SpriteManager():

    def __init__(self, screen_width: int, screen_height: int, sprite_asset_path: str):
        SPRITE_W = 16
        SPRITE_H = 16

        self.SPRITE_SCALE_W = screen_width / SPRITE_W 
        self.SPRITE_SCALE_H = screen_height / SPRITE_H 

        with open(sprite_asset_path, "r", encoding="utf-8") as f:
            self.sheet = json.loads(f.read(), object_hook=customJsonDecoder)

    
    def get_sprite_length(self, level: StageLevel):
        return len(self.sheet.stages[level.value].sprites)
    
    def draw_sprite(self, level: StageLevel, sprite_index: int, callback):
        sprites = self.sheet.stages[level.value].sprites

        for y, row in enumerate(sprites[sprite_index]):
            for x, v in enumerate(row):
                if v != "█":
                    continue

                left   = round(x * self.SPRITE_SCALE_W)
                top    = round(y * self.SPRITE_SCALE_H)
                right  = round((x + 1) * self.SPRITE_SCALE_W)
                bottom = round((y + 1) * self.SPRITE_SCALE_H)

                callback(left, top, right, bottom)
