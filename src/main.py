import pygame

from resources.sprite_manager import SpriteManager
from utils.utils import StageLevel
from utils.state import State

# Environment settings
SCREEN_W = 255
SCREEN_H = 255

SPRITE_INTERVAL = 1.0  # seconds

SPRITE_ASSET_PATH = "./assets/sprites.json"

# pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
clock = pygame.time.Clock()
running = True
dt = 0

# State
state = State()

sprite_index = 0
elapsed_time = 0.0

cicles = 0

# Callbacks
def draw_screen(left, top, right, bottom):
    rect = pygame.Rect(left, top, right - left, bottom - top)
    pygame.draw.rect(screen, "yellow", rect)


# Main Script

if __name__ == "__main__":
    sprite_manager = SpriteManager(SCREEN_W, SCREEN_W, SPRITE_ASSET_PATH)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if cicles >= 10:
            state.STAGE_LEVEL = StageLevel.LEVEL_1
            sprite_index = 0

        screen.fill("black")
        
        if elapsed_time >= SPRITE_INTERVAL:
            elapsed_time = 0.0
            sprite_index += 1
            cicles += 1

            if sprite_index >= sprite_manager.get_sprite_length(state.STAGE_LEVEL):
                sprite_index = 0
                

        # Draw Sprite
        sprite_manager.draw_sprite(state.STAGE_LEVEL, sprite_index, draw_screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000
        elapsed_time += dt

    pygame.quit()