import os
import json

class Language:
    def __init__(self, langDir = './lang/') -> None:
        self.langDir = langDir
    
    def langIdxToJson(self, idx):
        idxLang = 0
        for langFile in os.listdir(self.langDir):
            langPath = os.path.join(self.langDir, langFile)
            if (os.path.isfile(langPath)):
                if idxLang == idx:
                    with open(langPath) as lang:
                        return json.load(lang)
                idxLang += 1
        return None

    def chooseLang(self):
        print('Please, choose a language:')
        idxLang = 0
        for langFile in os.listdir(self.langDir):
            langPath = os.path.join(self.langDir, langFile)
            if (os.path.isfile(langPath)):
                with open(langPath) as lang:
                    langJson = json.load(lang)
                    print(idxLang, langJson['general']['lang'])
                idxLang += 1
        choosed = None
        print()
        while (choosed == None or choosed < 0 or choosed >= idxLang):
            choosed = int(input('Select the index of a valid lang: '))
        return self.langIdxToJson(choosed)