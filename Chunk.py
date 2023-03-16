from Cell import Cell
import math
class Chunk:
    def __init__(self, size, chunksX, chunksY, cellSize) -> None:
        self.size = size
        self.chunksX = chunksX
        self.chunksY = chunksY

        self.cursorX = 0
        self.cursorY = 0

        self.cellSize = cellSize

        self.cells = [ [ None for _ in range(self.size) ] for _ in range(self.size) ]

    def chunkToGrid(self, chunkX, chunkY, posX, posY):
        diffCols = self.chunksX // 2
        diffRows = self.chunksY // 2

        rangeCols = range(-diffCols, diffCols + 1) # Straight Colums
        rangeRows = range(diffRows, - diffRows - 1, -1) # Reverse Rows

        selChunkX = rangeCols[chunkX]
        selChunkY = rangeRows[chunkY]

        diffChunk = math.ceil(self.size / 2)

        cellX = 0
        cellY = 0

        if selChunkX == 0:
            cellX = (- (self.size // 2)) + posX
        elif selChunkX > 0:
            cellX = (posX + diffChunk) + abs((selChunkX - 1) * self.size)
        elif selChunkX < 0:
            cellX = - (diffChunk + ((self.size - 1) - posX) + abs((selChunkX + 1) * self.size))

        if selChunkY == 0:
            cellY = - ((- (self.size // 2)) + posY)
        elif selChunkY > 0:
            cellY = diffChunk + ((self.size - 1) - posY) + abs((selChunkY - 1) * self.size)
        elif selChunkY < 0:
            cellY = - ((posY + diffChunk) + abs((selChunkY + 1) * self.size))
        
        # print('cell', cellX, cellY)
        # print('pos', posX, posY)
        # print('diffChunk', diffChunk)
        # print('chunk', selChunkX, selChunkY)
        
        return (cellX, cellY)
    
    def gridToChunk(self, gridX, gridY, chunkX, chunkY):
        # print('cell', gridX, gridY)
        # print('chunks', chunkX, chunkY)
        
        diffChunk = math.ceil(self.size / 2)

        if chunkX == 0:
            posX = gridX + (self.size // 2)
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

    def addCell(self, chunkX, chunkY, type):
        gridX, gridY = self.chunkToGrid(chunkX, chunkY, self.cursorX, self.cursorY)
        # print('addCel', gridX, gridY)
        self.cells[self.cursorY][self.cursorX] = Cell(gridX, gridY, self.cellSize, type = type)

        if self.cursorX + 1 < self.size:
            self.cursorX += 1
        else:
            self.cursorX = 0
            self.cursorY += 1
    
    def getMidCell(self):
        return self.cells[2][2]
    
    def print(self):
        for y in self.cells:
            print()
            for x in y:
                x.print()