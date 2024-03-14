import time
import keyboard
import sys
from pyautogui import *

run = False  # Initialize run as False

def start():
    global run
    run = True

def pause():
    global run
    run = False

def stop():
    print("Program stopped.")
    sys.exit()

keyboard.add_hotkey('ctrl+shift', start)  # Press Ctrl + Shift to start
keyboard.add_hotkey('ctrl+alt', pause)     # Press Ctrl + Alt to pause
keyboard.add_hotkey('ctrl+s', stop)        # Press Ctrl + S to stop

while True:
    while run:
        time.sleep(10)
        moveRel(0, 10)
        moveRel(-10, 0)
        moveRel(0, -10)
        moveRel(10, 0)
