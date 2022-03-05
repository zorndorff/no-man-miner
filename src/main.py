import pyautogui;
import random;

RANDOM_RANGEX=100
RANDOM_RANGEY=100

pyautogui.keyDown('w') 

while True:
    randX=random.randrange(-RANDOM_RANGEX, RANDOM_RANGEX)
    randY=random.randrange(-RANDOM_RANGEY, RANDOM_RANGEY)
    print(f"Randomly moving X:{randX} Y:{randY}")
    pyautogui.moveRel(randX, randY, duration=3)  # move mouse relative to its current position
    pyautogui.leftClick(x=None, y=None, interval=1, duration=3)
