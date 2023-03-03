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
    count = 0
    for item in os.listdir(dirPath):
        itemPath = os.path.join(dirPath, item)
        count += 1
    return count