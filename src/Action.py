# Click APIs
import pyautogui as pag
from pynput.mouse import Button, Controller

import time

class Action:
    def __init__(self, confidence = .8) -> None:
        self.confidence = confidence
        self.mouse = Controller()
    
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
    
    def keyDown(self, key, sleep1 = .1, sleep2 = .2):
        pag.keyDown(key)
        time.sleep(sleep1)
        pag.keyUp(key)
        time.sleep(sleep2)