import pyautogui
from PIL import Image, ImageGrab
import time


def hit(key):
    pyautogui.keyDown(key)
    return


def iscollide(data):
    for i in range(185, 355):
        for j in range(435, 460):
            if data[i, j] < 100:
                return True
    return False


def iscollide1(data):
    for i in range(185, 355):
        for j in range(250, 435):
            if data[i, j] < 100:
                return True
    return False


if __name__ == "__main__":
    print("dino game starting in 1 seconds")
    time.sleep(1)
    while True:
        image = ImageGrab.grab().convert("L")
        data = image.load()
        if iscollide(data):
            hit("up")
        elif iscollide1(data):
            hit("down")
