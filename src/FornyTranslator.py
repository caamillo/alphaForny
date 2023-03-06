import time

from pynput.keyboard import Key

class FornyTranslator:
    def __init__(self, scriptPath, action, t, clear) -> None:
        self.scriptPath = scriptPath
        self.actions = action
        self.t = t
        self.cmds = self.getCmds()
        self.clear = clear

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
                    cmds[lastCmd] = []
                else:
                    splittedLine = normalizedLine.split()
                    if len(splittedLine) > 1:
                        if splittedLine[1].find(',') >= 0:
                            splittedLine[1] = splittedLine[1].split(',')
                        key, value = splittedLine[:2]
                        # print(self.mapKey(value))
                        if not self.validateCmd(key, value):
                            raise Exception(f'{ key } { value } { self.t("translator.notvalid") }')
                        cmds[lastCmd].append({ key: value })
                    else:
                        if not self.validateCmd(splittedLine[0]):
                            raise Exception(f'{ splittedLine[0] } { self.t("translator.notvalid") }')
                        cmds[lastCmd].append(splittedLine[0])
                    # print(splittedLine)
        except Exception as err:
            self.clear.clearScreen()
            print(f'[{ self.t("general.status.error") }]:', err)
        return cmds
    
    def mapKey(self, key):
        if key == 'UP':
            return Key.up
        elif key == 'DOWN':
            return Key.down
        elif key == 'RIGHT':
            return Key.right
        elif key == 'LEFT':
            return Key.left
        elif key == 'SHIFT':
            return Key.shift
        elif type(key) is str:
            return key.lower()
        return None

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
            elif key == 'PRESS':
                if type(value) is str and not (type(self.mapKey(key)) is None):
                    return True
            elif key == 'HOLD':
                if type(value) is str and not (type(self.mapKey(key)) is None):
                    return True
            elif key == 'RELEASE':
                if type(value) is str and not (type(self.mapKey(key)) is None):
                    return True
            elif key == 'SPAM':
                if type(value) is str and not (type(self.mapKey(key)) is None):
                    return True
            elif key == 'STOPSPAM':
                if type(value) is str and not (type(self.mapKey(key)) is None):
                    return True
            elif key == 'UNTIL':
                if type(value) is str:
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
        elif key == 'PRESS':
            self.actions.pressKey(self.mapKey(value))
        elif key == 'HOLD':
            self.actions.holdKey(self.mapKey(value))
        elif key == 'RELEASE':
            self.actions.releaseKey(self.mapKey(value))
        elif key == 'SPAM':
            self.actions.createSpam(self.mapKey(value))
        elif key == 'STOPSPAM':
            self.actions.destroySpam()
        elif key == 'UNTIL':
            self.actions.waitFor(value, until = True)

if __name__ == "__main__":
    trans = FornyTranslator('./scripts/EVs/Unima/Sp. Attack.txt')
    print(trans.getCmds())