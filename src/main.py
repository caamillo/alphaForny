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

osName = platform.system()
with open(f'./cmd/{ "windows" if osName == "Windows" else "linux" }.json') as f:
    cmd = json.load(f)

# Utils
# from utils import

# Language Setup
language = Language(STARTDIR, cmd)
lang = language.chooseLang()
translator = Translator(lang)
t = translator.t

# Script Setup
from Script import Script
def loadScript():
    chose = None
    script = Script(STARTDIR, 'scripts', t, cmd)

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

if __name__ == "__main__":
    script = loadScript()