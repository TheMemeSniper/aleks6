from pynput.keyboard import Key, Controller as keyboardController
from pynput.mouse import Button, Controller as mouseController
import time

keyboard = keyboardController()
mouse = mouseController()

print("WARNING! This program will press 6 and click every few seconds! If you do not want this to happen, press CTRL+C now.")
print("This program assumes you have blacklisted the Explaination button on the page using an extension such as uBlock Origin.")
print("It also assumes you have left your mouse cursor on top of the Check button.")
time.sleep(10)
print("Program not interrupted, continuing...")
while True:
    for x in range(10):
        keyboard.press("6")
        keyboard.release("6")
        time.sleep(0.3)
        keyboard.press(Key.backspace)
        keyboard.release(Key.backspace)
        time.sleep(0.3)
    keyboard.press("6")
    keyboard.release("6")
    mouse.press(Button.left)
    mouse.release(Button.left)