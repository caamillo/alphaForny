from Chunk import Chunk
import math

class Map:
    def __init__(self, chunksToLoadX, chunksToLoadY, chunkSize) -> None:
        self.chunksX = chunksToLoadX
        self.chunksY = chunksToLoadY
        self.chunkSize = chunkSize

        self.map = [ [ Chunk(chunkSize) for _ in range(self.chunksX) ] for _ in range(self.chunksY) ]
    def addCell(self, cell):
        chunkX = round(cell.gridX / self.chunkSize)
        chunkY = round(cell.gridY / self.chunkSize)

        self.map[chunkY][chunkX].addCell(cell, chunkX, chunkY)
    def getCell(self, x, y):
        diffX = round(x / self.chunkSize)
        diffY = round(y / self.chunkSize)

        print('diffs', diffX, diffY)
        print('chunkToLoad', self.chunksX, self.chunksY)

        chunkX = (self.chunksX // 2) + diffX
        chunkY = (self.chunksY // 2) + diffY

        print('chunks', chunkX, chunkY)

        return self.map[chunkY][chunkX].cells[y - (chunkY * self.chunkSize)][x - (chunkX * self.chunkSize)]
    def getMidChunk(self):
        return self.map[math.ceil(self.chunksY / 2)][math.ceil(self.chunksX / 2)]
    def print(self):
        for y in self.map:
            print()
            for x in y:
                x.print()
                print(' - ', end='')