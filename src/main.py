# Libs
import toml
import os

# Language
from Language import Language
from Translator import Translator

# Config Setup
from Config import Config
config = Config()

STARTDIR = config.general['STARTDIR']

# Utils
from utils import printDir

# Language Setup
language = Language(langDir = STARTDIR)
lang = language.chooseLang()
translator = Translator(lang)
t = translator.t

def loadScript():
    os.system('clear')
    print(t('main.select'))

    choosed = None
    selectedPath = STARTDIR
    selectedDirName = 'scripts'

    selectedDir = f'{ selectedPath }{ selectedDirName }/'
    # printTree(selectedDir)
    while (choosed == None):
        printDir(selectedDir, t)
        break

if __name__ == "__main__":
    loadScript()
    # print(t('general.name'))