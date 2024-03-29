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
from utils import Clear
clear = Clear(False)

# Language Setup
# language = Language(STARTDIR, clear)          [ DEBUG ]
# lang = language.chooseLang()                  [ DEBUG ]
with open('./lang/en.json') as f:
    translator = Translator(json.load(f))
t = translator.t

# Script Setup
from Script import Script
def loadScript():
    chose = None
    script = Script(STARTDIR, 'scripts', t, clear)

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
    scriptPath = './scripts/Exp/Spiraria.txt' # loadScript()
    alphaForny = AlphaForny(scriptPath, t, clear)
    alphaForny.start()