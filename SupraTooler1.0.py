from pynput import keyboard
import pyautogui
import time
from ACCIart import art
state = "COMERCE"
def StarupTelemetry(): 
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

StarupTelemetry()

pressed = set()

def ToTopBar():
    pyautogui.moveTo(1200, 0)
    pyautogui.click()

def ToBottomBar():
    pyautogui.moveTo(1100, 1350)
    pyautogui.click()

def ToTopLeftBar():
    pyautogui.moveTo(10, 15)

def on_press(key):
    pressed.add(key)

    try:

        if keyboard.Key.cmd in pressed and key.char == "3":
            ToTopBar()
            
        elif keyboard.Key.shift in pressed and keyboard.Key.space in pressed:
            ToBottomBar()


        elif keyboard.Key.cmd in pressed and key.char == "2":
            ToTopLeftBar()
        
    except:
        pass

def on_release(key):
    try:
        pressed.discard(key)
    except:
        pass
