from Language import Language
from Translator import Translator

language = Language()

def choosePath():
    print('Select a script:')

if __name__ == "__main__":
    lang = language.chooseLang()
    translator = Translator(lang)
    t = translator.t
    # print(t('general.name'))