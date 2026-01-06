import time
import sys
import json

with open("./sprites.json", "r") as f:
    sprites = json.load(f)

H = len(sprites["egg"][0])

def draw(frame):
    # Move cursor up H lines (to the start of the previous frame)
    sys.stdout.write(f"\033[{H}A")
    # Clear each line and redraw
    for line in frame:
        sys.stdout.write("\033[2K\r")  # clear line
        sys.stdout.write(line + "\n")
    sys.stdout.flush()

# Print once to create space for the sprite (so moving up works)
print("\n" * H, end="")

# Example loop: redraw the same sprite repeatedly
for i in range (0, 10):
    for sprite in sprites["egg"]:
        draw(sprite)
        time.sleep(0.5)