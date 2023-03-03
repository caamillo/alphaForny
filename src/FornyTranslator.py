class FornyTranslator:
    def __init__(self, scriptPath) -> None:
        self.scriptPath = scriptPath
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
        return cmds

trans = FornyTranslator('./scripts/EVs/Unima/Sp. Attack.txt')
print(trans.getCmds())