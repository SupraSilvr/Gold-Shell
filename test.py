import pyautogui
from pynput import keyboard

pressed = set()

def on_pressed(key):
	pressed_add(key)
	
if keyboard.Key.cmd in pressed:
	print("code Working")

def on_release(key):
	try:
		pressed.discard(key)
	except:
		pass

