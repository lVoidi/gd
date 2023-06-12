import keyboard
import pyautogui
import time

pyautogui.FAILSAFE = False

on_runtime = True

def on_cancel() -> None:
    global on_runtime
    on_runtime = False

def center_mouse() -> None: 
    global on_runtime
    """
    This function will center the mouse using pyautogui
    """
    width, height = pyautogui.size()
    screen_center = (width/2, height/2)
    while on_runtime:
        pyautogui.moveTo(*screen_center)
        time.sleep(0.1)
        if keyboard.is_pressed("y"):
            on_runtime = False
        elif keyboard.is_pressed("x"):
            exit()

while True:
    if keyboard.is_pressed("ctrl+shift+t"):
        on_runtime = True
        center_mouse()
