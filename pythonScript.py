import pyautogui, sys
from datetime import datetime
import time, threading

def main():
    print(pyautogui.position())
    size = pyautogui.size()
    print(size)

    width = size.width / 2
    height = size.height / 2

    startx = width + 200
    starty = height + 100
    endx = size.width - 20
    endy = size.height - 20
    xit = 240
    yit = 120
    num_seconds = 1
    x = startx
    y = starty

    pyautogui.moveTo(x, y, duration=0)
    pyautogui.click(x, y)

    print('Initialized Successfully at {}'.format(datetime.now()))

    while True:

        x = x + xit
        y = y + yit
        if(x > endx or x < startx or y > endy or y < starty):
            x = startx
            y = starty
        pyautogui.moveTo(x, y, duration=num_seconds)
        #duration in seconds to move mouse around
        time.sleep(300)

        if(x + xit > endx):
            pyautogui.click(x, y)

if __name__ == "__main__":
    main()
