from pynput import keyboard
import pyautogui
import time
from ACCIart import art
state = "0"
state = "COMERCE"
def StartupTelemetry(): 
    time.sleep(0.5)
    print("APP STARTED")
    time.sleep(0.5)
    print("SupraTooler ver 1.0.1")
    time.sleep(0.1)
    print(f"Operation: {state} state")
    time.sleep(0.6)
    print("Made by GoldShell")
    time.sleep(0.1)
    print("SupraTooler, keeping your eyes on the prize")
    time.sleep(0.2)
    print(art)

if state == "COMERCE":
	StartupTelemetry()
else:
	pass
pressed = set()

def ToTopBar():
    pyautogui.moveTo(2000, 0)
    pyautogui.click()

def ToBottomBar():
    pyautogui.moveTo(1100, 1500)
    pyautogui.click()



def on_press(key):
    pressed.add(key)

    try:
        if keyboard.Key.cmd in pressed:
            ToTopBar()

        elif keyboard.Key.shift in pressed:
            ToBottomBar()
    except:
        pass
def on_release(key):

    try:
        pressed.discard(key)
    except:
        pass

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
