import pyautogui
import time
def hit(key):
    pyautogui.keyDown(key)
    return
word=input("Enter the text to auto type: ")
time.sleep(2)
while True:
    pyautogui.PAUSE=0.1
    # hit("w")
    pyautogui.typewrite(word)
    hit("Enter")