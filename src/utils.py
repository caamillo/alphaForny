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