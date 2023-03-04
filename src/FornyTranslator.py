import time

from utils import clearScreen

class FornyTranslator:
    def __init__(self, scriptPath, action) -> None:
        self.scriptPath = scriptPath
        self.actions = action
        self.cmds = self.getCmds()

    def normalizeRow(self, row):
        if row.find('#') >= 0: # Trim Row + Remove Comments
            return row.strip()[ : - (len(row) - row.find('#'))]
        else:
            return row.strip()

    def getCmds(self):
        lines = open(self.scriptPath, 'r').readlines()

        cmds = {}
        lastCmd = ""

        try:
            for line in lines:
                normalizedLine = self.normalizeRow(line)
                if len(normalizedLine) <= 0:
                    pass # Skip blank \n
                elif normalizedLine.find(':') >= 0:
                    lastCmd = normalizedLine[ : - (len(normalizedLine) - normalizedLine.find(':'))]
                    cmds[lastCmd] = {}
                else:
                    splittedLine = normalizedLine.split()
                    if len(splittedLine) > 1:
                        if splittedLine[1].find(',') >= 0:
                            splittedLine[1] = splittedLine[1].split(',')
                        key, value = splittedLine[:2]
                        if not self.validateCmd(key, value):
                            raise Exception(f'{ key } { value } is not a valid command')
                        cmds[lastCmd][key] = value
                    else:
                        if not self.validateCmd(splittedLine[0]):
                            raise Exception(f'{ splittedLine[0] } is not a valid command')
                        cmds[lastCmd][splittedLine[0]] = splittedLine[0]
                    # print(splittedLine)
        except Exception as err:
            clearScreen()
            print('[Error]:', err)
        
        return cmds

    def validateCmd(self, key, value = None):
        try:
            if key == 'CLICK':
                if type(value) is list and len(value) > 1:
                    val1, val2 = map(int, value[:2])
                    if type(val1) is int and type(val2) is int:
                        return True
            elif key == 'SLEEP':
                val1 = float(value)
                if type(val1) is float:
                    return True
            elif key == 'WAITFOR':
                if type(value) is str:
                    return True
            elif key == 'PRINT':
                if type(value) is str:
                    return True
            elif key == 'WAITBATTLE':
                if type(value) is None:
                    return True
            elif key == 'SKIP':
                if type(value) is None:
                    return True
            return False
        except:
            return False
        
    
    def translateCmd(self, key, value = None):
        if key == 'CLICK':
            clickX, clickY = map(int, value[:2])
            self.actions.clickTo(clickX, clickY)
        elif key == 'SLEEP':
            time.sleep(float(value))
        elif key == 'WAITFOR':
            self.actions.waitFor(value)
        elif key == 'PRINT':
            print(value)

if __name__ == "__main__":
    trans = FornyTranslator('./scripts/EVs/Unima/Sp. Attack.txt')
    print(trans.getCmds())