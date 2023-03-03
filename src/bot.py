# Win APIs
import win32api, win32con
import pyautogui as pag

import time

class Bot:
    def __init__(self, confidence = .8) -> None:
        self.confidence = confidence
    
    def clickTo(self, x, y, sleep1 = .1, sleep2 = .5):
        win32api.SetCursorPos((x, y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(sleep1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        time.sleep(sleep2)
    
    def isOnScreen(self, what) -> bool:
        return pag.locateOnScreen(f'../refs/{ what }.png', grayscale = True, confidence = self.confidence) != None
    
    def waitFor(self, what, sleep = 1):
        while True:
            if self.isOnScreen(what):
                break
            time.sleep(sleep)
    
    def keyDown(self, key, sleep1 = .1, sleep2 = .2):
        pag.keyDown(key)
        time.sleep(sleep1)
        pag.keyUp(key)
        time.sleep(sleep2)