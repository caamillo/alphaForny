# Win APIs
import win32api, win32con
import pyautogui as pag

import time

class Bot:
    def __init__(self) -> None:
        pass
    def clickTo(self, x, y):
        win32api.SetCursorPos((x, y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        time.sleep(.5)