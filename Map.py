from Chunk import Chunk
import math

class Map:
    def __init__(self, chunksToLoadX, chunksToLoadY, chunkSize, cellSize) -> None:
        self.chunksX = chunksToLoadX
        self.chunksY = chunksToLoadY
        self.chunkSize = chunkSize
        self.cellSize = cellSize

        self.map = [ [ Chunk(chunkSize, self.chunksX, self.chunksY, self.cellSize) for _ in range(self.chunksX) ] for _ in range(self.chunksY) ]
    def addCell(self, chunkX, chunkY, type):
        self.map[chunkY][chunkX].addCell(type)
    def getCell(self, x, y):
        diffX = round(x / self.chunkSize)
        diffY = round(y / self.chunkSize)

        # print('diffs', diffX, diffY)
        # print('chunkToLoad', self.chunksX, self.chunksY)

        chunkX = (self.chunksX // 2) + diffX
        chunkY = (self.chunksY // 2) + diffY

        # print('chunks', diffX, diffY)

        posX, posY = self.map[chunkY][chunkX].gridToChunk(x, y, diffX, diffY)

        # print('cell', x, y, 'relpos', posX, posY)
        # print('chunk', self.map[chunkY][chunkX].cells[posY])

        return self.map[chunkY][chunkX].cells[posY][posX]
    def getMidChunk(self):
        return self.map[math.ceil(self.chunksY / 2)][math.ceil(self.chunksX / 2)]
    def print(self):
        for y in self.map:
            print()
            for x in y:
                x.print()
                print(' - ', end='')