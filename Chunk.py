import math

class Chunk:
    def __init__(self, size) -> None:
        self.size = size
        self.cels = [ [ None for _ in range(self.size) ] for _ in range(self.size) ]
    def gridToChunk(self, cel, chunkX, chunkY):
        diffChunk = math.ceil(self.size / 2)

        posX = abs(cel.gridX) - (diffChunk + abs(((chunkX - 1) if chunkX >= 0 else (chunkX + 1)) * self.size))
        posY = abs(cel.gridY) - (diffChunk + abs(((chunkY - 1) if chunkY >= 0 else (chunkY + 1)) * self.size))

        posX = posX if chunkX != 0 else cel.gridX + (self.size // 2)
        posX = posY if chunkY != 0 else cel.gridY + (self.size // 2)

        return (posX, posY)
    def addCel(self, cel, chunkX, chunkY):
        posX, posY = self.gridToChunk(cel, chunkX, chunkY)
        print('relPos', posX, posY)
        self.cels[posY][posX] = cel
    def getMidCel(self):
        return self.cels[2][2]
    def print(self):
        for y in self.cels:
            print()
            for x in y:
                x.print()