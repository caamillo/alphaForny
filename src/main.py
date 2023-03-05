# Libs
import os
import platform
import json

# AlphaForny Core
from AlphaForny import AlphaForny

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
        idx = int(input(f'{ t("main.select2") }: '))
        
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

if __name__ == "__main__":
    scriptPath = './scripts/EVs/Unima/Sp. Attack.txt' # loadScript()
    alphaForny = AlphaForny(scriptPath, t)
    alphaForny.start()