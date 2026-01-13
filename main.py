import pygame

from sprite_manager import SpriteManager
from tools.utils import StageLevel

# Environment settings
SCREEN_W = 255
SCREEN_H = 255

SPRITE_W = 16
SPRITE_H = 16

SPRITE_SCALE_W = SCREEN_W / SPRITE_W 
SPRITE_SCALE_H = SCREEN_H / SPRITE_H 

SPRITE_INTERVAL = 1.0  # seconds

# pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
clock = pygame.time.Clock()
running = True
dt = 0

# Sprites
sprite_manager = SpriteManager()


sprint_index = 0
elapsed_time = 0.0

sprites = sprite_manager.get_sprites(StageLevel.LEVEL_0)

cicles = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if cicles >= 10:
        sprites = sprite_manager.get_sprites(StageLevel.LEVEL_1)

    screen.fill("black")
    
    if elapsed_time >= SPRITE_INTERVAL:
        elapsed_time = 0.0
        sprint_index += 1
        cicles += 1

        if sprint_index >= len(sprites):
            sprint_index = 0

    for y, row in enumerate(sprites[sprint_index]):
        for x, v in enumerate(row):
            if v != "█":
                continue

            left   = round(x * SPRITE_SCALE_W)
            top    = round(y * SPRITE_SCALE_H)
            right  = round((x + 1) * SPRITE_SCALE_W)
            bottom = round((y + 1) * SPRITE_SCALE_H)

            rect = pygame.Rect(left, top, right - left, bottom - top)
            pygame.draw.rect(screen, "yellow", rect)

    pygame.display.flip()

    dt = clock.tick(60) / 1000
    elapsed_time += dt

pygame.quit()