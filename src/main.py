# Libs
import os

# Language
from Language import Language
from Translator import Translator

# Config Setup
from Config import Config
config = Config()

STARTDIR = config.general['STARTDIR']

# Utils
# from utils import 

# Language Setup
language = Language(langDir = STARTDIR)
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
            if (os.path.isdir(item)):
                script.gotoDir(idx)
            else:
                chose = item
        elif (idx == -1):
            script.backDir()
    
    print('chose', chose)

if __name__ == "__main__":
    loadScript()
    # print(t('general.name'))