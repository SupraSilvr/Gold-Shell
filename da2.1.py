from pynput import keyboard
import pyautogui
import time
from ACCIart import art
state = "0"
state = "Dev"
def StartupTelemetry(): 
    time.sleep(0.5)
    print("APP STARTED")
    time.sleep(0.5)
    print("SupraTooler ver 2.5.5")
    time.sleep(0.1)
    print(f"Operation: {state} state")
    time.sleep(0.6)
    print("Made by GoldShell")
    time.sleep(0.1)
    print("SupraTooler, keeping your eyes on the prize")
    time.sleep(0.2)
    print(art)
StartupTelemetry()
pressed = set()

width, height = pyautogui.size()
w = width/2
def ToTopBar():
    pyautogui.moveTo(width, 0)

def ToBottomBar():
    pyautogui.moveTo(w, height)

def close():
	pyautogui.moveTo(0, 0)
def finder():
    pyautogui.moveTo(200, 1500)
def on_press(key):
    pressed.add(key)
    try:
        if keyboard.Key.f1 in pressed:
            ToTopBar()
        elif keyboard.Key.f2 in pressed:
            ToBottomBar()
        elif len(pressed) == 2 and keyboard.Key.cmd and keyboard.KeyCode.from_char('w'):
            close()
        elif keyboard.Key.f3 in pressed:
            finder()
    except:
        pass
def on_release(key):

    try:
        pressed.discard(key)
    except:
        pass

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
