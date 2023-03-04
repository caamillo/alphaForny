import time

class FornyTranslator:
    def __init__(self, scriptPath, action) -> None:
        self.scriptPath = scriptPath
        self.actions = action

    def normalizeRow(self, row):
        if row.find('#') >= 0: # Trim Row + Remove Comments
            return row.strip()[ : - (len(row) - row.find('#'))]
        else:
            return row.strip()

    def getCmds(self):
        lines = open(self.scriptPath, 'r').readlines()

        cmds = {}
        lastCmd = ""

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
                    cmds[lastCmd][splittedLine[0]] = splittedLine[1]
                else:
                    cmds[lastCmd][splittedLine[0]] = splittedLine[0]
                print(splittedLine)
        
        return cmds

    def validateCmd(self, key, value):
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
                if value is str:
                    return True
            elif key == 'WAITBATTLE':
                if value is None:
                    return True
            elif key == 'SKIP':
                if value is None:
                    return True
            return False
        except:
            return False
        
    
    def translateCmd(self, key, value):
        if key.find('CLICK') >= 0:
            # clickX, clickY = value[:2]
            self.actions.clickTo(value[0], value[1])
        elif key.find('SLEEP') >= 0:
            time.sleep(value)
        elif key.find('WAITFOR') >= 0:
            self.actions.waitFor(value)
        elif key.find('WAITBATTLE') >= 0:
            self.actions.waitBattle()
        elif key.find('SKIP') >= 0:
            self.actions.skip()

if __name__ == "__main__":
    trans = FornyTranslator('./scripts/EVs/Unima/Sp. Attack.txt')
    print(trans.getCmds())