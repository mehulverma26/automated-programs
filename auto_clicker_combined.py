import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

key = input("Enter the key for the autoclicker(left, right or middle): ")
if "left" in key or "LEFT" in key or "Left" in key or "left click" in key:
    button = Button.left
elif "right" in key or "Right" in key or "RIGHT" in key or "right click" in key:
    button = Button.right
else:
    button = Button.middle
clicking_time = float(input("enter the delay for the autoclicker(for eg. 0.5): "))
start_key = input("enter the start and stop key: ")
end_key = input("enter the end key: ")
print("the start and stop key is", start_key, "and the exit key is", end_key)
delay = clicking_time
start_stop_key = KeyCode(char=start_key)
exit_key = KeyCode(char=end_key)


class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)


mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()


def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == exit_key:
        click_thread.exit()
        listener.stop()
        print("Exiting...")


with Listener(on_press=on_press) as listener:
    listener.join()
