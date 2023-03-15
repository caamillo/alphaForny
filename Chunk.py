import math

class Chunk:
    def __init__(self, size) -> None:
        self.size = size
        self.cells = [ [ None for _ in range(self.size) ] for _ in range(self.size) ]
    def gridToChunk(self, cell, chunkX, chunkY):
        diffChunk = math.ceil(self.size / 2)

        posX = abs(cell.gridX) - (diffChunk + abs(((chunkX - 1) if chunkX >= 0 else (chunkX + 1)) * self.size))
        posY = abs(cell.gridY) - (diffChunk + abs(((chunkY - 1) if chunkY >= 0 else (chunkY + 1)) * self.size))

        posX = posX if chunkX != 0 else cell.gridX + (self.size // 2)
        posX = posY if chunkY != 0 else cell.gridY + (self.size // 2)

        return (posX, posY)
    def addCell(self, cell, chunkX, chunkY):
        posX, posY = self.gridToChunk(cell, chunkX, chunkY)
        print('relPos', posX, posY)
        self.cells[posY][posX] = cell
    def getMidCell(self):
        return self.cells[2][2]
    def print(self):
        for y in self.cells:
            print()
            for x in y:
                x.print()