import pygame
from pynput import keyboard
import pyautogui
from ACCIart import art

state = "COMERCE"
pressed = set()

def StarupTelemetry():
    pygame.init()

    screen = pygame.display.set_mode((900, 500))
    pygame.display.set_caption("SupraTooler")

    font = pygame.font.SysFont("Courier", 24)

    lines = [
        "APP STARTED",
        "SupraTooler ver 1.0.1",
        f"Operation: {state} state",
        "Made by GoldShell",
        "",
        art
    ]

    screen.fill((0, 0, 0))

    y = 20
    for line in lines:
        for subline in line.split("\n"):
            text = font.render(subline, True, (255, 255, 255))
            screen.blit(text, (20, y))
            y += 25

    pygame.display.flip()
    pygame.time.wait(2500)
    pygame.quit()


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
    pressed.discard(key)


# RUN FLOW
StarupTelemetry()

listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()
listener.join()