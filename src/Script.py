# Lib
import os

# Utils
from utils import countChildren

class Script:
    def __init__(self, selectedPath, selectedDirName, t) -> None:

        selectedDir = f'{ selectedPath }{ selectedDirName }/'
        self.scriptDir = selectedDir

        self.currentPath = selectedDir

        self.t = t
        self.depth = 0
        self.count = countChildren(selectedDir)

    def idxItemToPath(self, idx):
        return os.path.join(self.currentPath, os.listdir(self.currentPath)[idx])
    
    def isStart(self):
        return self.depth == 0

    def gotoDir(self, idx):
        if (idx > self.count or idx < 0):
            return
        self.depth += 1
        self.currentPath = self.idxItemToPath(idx)

    def backDir(self):
        if (self.depth > 0):
            self.depth -= 1
            self.currentPath = '.' + os.path.dirname(self.currentPath)[1:]

    def printCurrDir(self):
        os.system('clear')
        print(self.t('main.select'))
        for (idx, item) in enumerate(os.listdir(self.currentPath)):
            itemPath = os.path.join(self.currentPath, item)
            isDir = os.path.isdir(itemPath)
            spaces = len(str(len(os.listdir(self.currentPath)))) - (len(str(idx)) - 1)
            sep = ''

            for _ in range(spaces):
                sep += ' '
            
            print('{}{}[{}] {}'.format(idx, sep, '+' if isDir else '-', item), end='' if isDir else '\n')

            if (isDir):
                if (self.count > 0):
                    print(f' ({ self.count } { self.t("main.item.items_found") })')
                else:
                    print(f' ({ self.t("main.item.empty") })')