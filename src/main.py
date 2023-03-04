# Libs
import os
import platform
import json

# Language
from Language import Language
from Translator import Translator

# Config Setup
from Config import Config
config = Config()

STARTDIR = config.general['STARTDIR']

# Utils
from utils import clearScreen

# Language Setup
language = Language(STARTDIR)
lang = language.chooseLang()
translator = Translator(lang)
t = translator.t

# Script Setup
from Script import Script
def loadScript():
    chose = None
    script = Script(STARTDIR, 'scripts', t)

    while (chose == None):
        script.printCurrDir()
        if (not script.isStart()):
            print(t('main.goback'), -1)
        idx = int(input('Select: '))
        
        if (idx >= 0):
            item = script.idxItemToPath(idx)
            if (item == None):
                continue
            elif (os.path.isdir(item)):
                script.gotoDir(idx)
            else:
                chose = item
        elif (idx == -1):
            script.backDir()
    return chose

from FornyTranslator import FornyTranslator
from Action import Action

if __name__ == "__main__":
    scriptPath = loadScript()
    action = Action()
    fornytrans = FornyTranslator(scriptPath, action)