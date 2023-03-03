import os

def printTree(dirPath, indent=''):
    for item in os.listdir(dirPath):
        itemPath = os.path.join(dirPath, item)
        if os.path.isdir(itemPath):
            print(f'{ indent }+ { item }/')
            printTree(itemPath, indent + ' ')
        else:
            print(f'{ indent }- { item }')

def countChildren(dirPath):
    numFiles = 0
    numDirs = 0
    for item in os.listdir(dirPath):
        itemPath = os.path.join(dirPath, item)
        if os.path.isfile(itemPath):
            numFiles += 1
        elif os.path.isdir(itemPath):
            numDirs += 1
    return numFiles + numDirs

def printDir(dirPath, t):
    for (idx, item) in enumerate(os.listdir(dirPath)):
        itemPath = os.path.join(dirPath, item)
        isDir = os.path.isdir(itemPath)
        spaces = len(str(len(os.listdir(dirPath)))) - (len(str(idx)) - 1)
        sep = ''
        for _ in range(spaces):
            sep += ' '
        print('{}{}[{}] {}'.format(idx, sep, '+' if isDir else '-', item), end='' if isDir else '\n')
        if (isDir):
            count = countChildren(itemPath)
            if (count > 0):
                print(f' ({ count } { t("main.item.items_found") })')
            else:
                print(f' ({ t("main.item.empty") })')