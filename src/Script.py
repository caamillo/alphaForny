# Lib
import os

# Utils
from utils import countChildren

class Script:
    def __init__(self, selectedPath, selectedDirName, t, cmd) -> None:

        selectedDir = f'{ selectedPath }{ selectedDirName }/'
        self.scriptDir = selectedDir

        self.currentPath = selectedDir

        self.t = t
        self.cmd = cmd
        self.depth = 0
        self.count = countChildren(selectedDir)

    def idxItemToPath(self, idx):
        if (idx < self.count and idx >= 0):
            return os.path.join(self.currentPath, os.listdir(self.currentPath)[idx])
    
    def isStart(self):
        return self.depth == 0

    def gotoDir(self, idx):
        if (idx >= self.count or idx < 0):
            return
        print(idx, self.currentPath, self.depth, self.count)
        self.depth += 1
        self.currentPath = self.idxItemToPath(idx)
        self.count = countChildren(self.currentPath)

    def backDir(self):
        if (self.depth > 0):
            self.depth -= 1
            self.currentPath = '.' + os.path.dirname(self.currentPath)[1:]
            self.count = countChildren(self.currentPath)

    def printCurrDir(self):
        os.system(self.cmd['general']['clear'])
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
                count = countChildren(itemPath)
                if (count > 0):
                    print(f' ({ count } { self.t("main.item.items_found") })')
                else:
                    print(f' ({ self.t("main.item.empty") })')