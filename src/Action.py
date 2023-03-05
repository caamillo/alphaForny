# Automate APIs
import pyautogui as pag

# Input APIs
import pynput.mouse as mouse
import pynput.keyboard as kbd

from pynput.mouse import Button
from pynput.keyboard import Key

import time

class Action:
    def __init__(self, confidence = .8) -> None:
        self.confidence = confidence
        
        self.mouse = mouse.Controller()
        self.kbd = kbd.Controller()
    
    def clickTo(self, x, y, left = True, sleep1 = .1, sleep2 = .5):
        self.mouse.position = (x, y)
        self.mouse.press(Button.left if left else Button.right)
        time.sleep(sleep1)
        self.mouse.release(Button.left if left else Button.right)
        time.sleep(sleep2)
    
    def isOnScreen(self, what) -> bool:
        return pag.locateOnScreen(f'../refs/{ what }.png', grayscale = True, confidence = self.confidence) != None
    
    def waitFor(self, what, sleep = 1):
        while True:
            if self.isOnScreen(what):
                break
            time.sleep(sleep)

    def holdKey(self, key):
        self.kbd.press(key)
    
    def releaseKey(self, key):
        self.kbd.release(key)
    
    def pressKey(self, key, sleep1 = .1, sleep2 = .2):
        self.holdKey(key)
        time.sleep(sleep1)
        self.releaseKey(key)
        time.sleep(sleep2)