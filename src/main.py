# Libs
import toml

# Language
from Language import Language
from Translator import Translator

# Config Setup
from Config import Config
config = Config()

# Language Setup
language = Language(lang = config.general['STARTDIR'])
lang = language.chooseLang()
translator = Translator(lang)
t = translator.t

def choosePath():
    print('Select a script:')
    choosed = None
    selectedDir = 'lang'
    # while (choosePath == None):
    #     for scriptDir in os.listdir(self.langDir):

if __name__ == "__main__":
    pass
    # print(t('general.name'))