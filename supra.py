from pynput import keyboard
import pyautogui
import time
from ACCIart import art
import pygame

pygame.init()
WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
icon = pygame.image.load("ico.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("SupraToole 1.1.1")
font = pygame.font.Font("Space_Mono/SpaceMono-Regular.ttf", 24)


clock = pygame.time.Clock()
clock.tick(60)

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False

screen.fill((0, 0, 0))

text = font.render("SupraTooler", True, (255, 255, 255))
text_rect = text.get_rect(center=(400, 250))
screen.blit(text, text_rect)
pygame.time.wait(2000)

pygame.display.flip()

pygame.quit()

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

def vim_down():
    pyautogui.press('down')

def vim_up():
    pyautogui.press('up')


def on_press(key):
    pressed.add(key)

    try:

        if keyboard.Key.cmd in pressed and key.char == "2":
            ToTopBar()
            
        elif keyboard.Key.shift in pressed and keyboard.Key.space in pressed:
            ToBottomBar()


        elif keyboard.Key.cmd in pressed and key.char == "3":
            ToTopLeftBar()
        
        elif keyboard.Key.cmd in pressed and keyboard.Key.caps_lock in pressed and key.char == "j":
            vim_down()
        elif keyboard.Key.cmd in pressed and keyboard.Key.caps_lock in pressed and key.char == "k":
            vim_up()

    except:
        pass

def on_release(key):
    try:
        pressed.discard(key)
    except:
        pass
