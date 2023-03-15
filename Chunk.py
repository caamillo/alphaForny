import math

class Chunk:
    def __init__(self, size) -> None:
        self.size = size
        self.cells = [ [ None for _ in range(self.size) ] for _ in range(self.size) ]
    
    def gridToChunk(self, gridX, gridY, chunkX, chunkY):
        print('cell', gridX, gridY)
        print('chunks', chunkX, chunkY)
        
        diffChunk = math.ceil(self.size / 2)

        if chunkX == 0:
            posX = abs(gridX) + (self.size // 2)
        elif gridX >= 0:
            posX = gridX - (diffChunk + abs((chunkX - 1) * self.size))
        elif gridX < 0:
            posX = (self.size - 1) + (gridX + (diffChunk + abs((chunkX + 1) * self.size)))
        
        if chunkY == 0:
            posY = abs(gridY) + (self.size // 2)
        elif gridY >= 0:
            posY = gridY - (diffChunk + abs((chunkY - 1) * self.size))
        elif gridY < 0:
            posY = (self.size - 1) + (gridY + (diffChunk + abs((chunkY + 1) * self.size)))
        
        return (posX, posY)

    def addCell(self, cell, chunkX, chunkY):
        posX, posY = self.gridToChunk(cell.gridX, cell.gridY, chunkX, chunkY)

        print('relPos', posX, posY)

        self.cells[posY][posX] = cell
    
    def getMidCell(self):
        return self.cells[2][2]
    
    def print(self):
        for y in self.cells:
            print()
            for x in y:
                x.print()