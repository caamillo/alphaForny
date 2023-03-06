# Automate APIs
import pyautogui as pag

# Input APIs
import pynput.mouse as mouse
import pynput.keyboard as kbd

from pynput.mouse import Button
from pynput.keyboard import Key

import time
from threading import Thread

class Action:
    def __init__(self, confidence = .85) -> None:
        self.confidence = confidence
        
        self.mouse = mouse.Controller()
        self.kbd = kbd.Controller()

        self.spam = False
    
    def clickTo(self, x, y, left = True, sleep1 = .1, sleep2 = .5):
        self.mouse.position = (x, y)
        self.mouse.press(Button.left if left else Button.right)
        time.sleep(sleep1)
        self.mouse.release(Button.left if left else Button.right)
        time.sleep(sleep2)
    
    def isOnScreen(self, what) -> bool:
        return pag.locateOnScreen(f'./refs/{ what }.png', grayscale = False, confidence = self.confidence) != None
    
    def waitFor(self, what, until = False, sleep = .1):
        while True:
            if until and (not self.isOnScreen(what)):
                break
            elif not until and self.isOnScreen(what):
                break
            print('Non Trovato')
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

    def spamKey(self, key, sleep1 = .1, sleep2 = .2, sleep3 = .5):
        while self.spam:
            print('Spamming', key)
            self.pressKey(key, sleep1, sleep2)
            time.sleep(sleep3)
    
    def createSpam(self, key, sleep1 = .1, sleep2 = .2, sleep3 = .5):
        self.spam = True
        spamThread =  Thread(target = self.spamKey, args=(key, sleep1, sleep2, sleep3))
        spamThread.start()
    
    def destroySpam(self):
        self.spam = False