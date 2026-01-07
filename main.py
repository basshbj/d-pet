import time
import sys
import json

from colorama import Fore

with open("./sprites.json", "r", encoding="utf-8") as f:
    sprites = json.load(f)

H = len(sprites["egg"][0])

def draw(frame):
    # Move cursor up H lines (to the start of the previous frame)
    sys.stdout.write(f"\033[{H}A")
    # Clear each line and redraw
    for line in frame:
        sys.stdout.write("\033[2K\r")  # clear line
        sys.stdout.write(Fore.YELLOW + line + Fore.RESET + "\n")
    sys.stdout.flush()

# Print once to create space for the sprite (so moving up works)
print("\n" * H, end="")

for i in range (0, 10):
    for sprite in sprites["egg"]:
        draw(sprite)
        time.sleep(0.5)
