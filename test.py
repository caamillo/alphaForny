from Map import Map

import math

cellSize = 30
chunkSize = 5

# Create Chunks
chunksToLoadX = 3
chunksToLoadY = 3

mapChunks = Map(chunksToLoadX, chunksToLoadY, chunkSize, cellSize)

print('chunkToLoad X / Y', chunksToLoadX, chunksToLoadY)

rangeCols = chunksToLoadX // 2
rangeRows = chunksToLoadY // 2

for chunkY in range(chunksToLoadY):
    # print('New Chunks-Row Added')
    for chunkX in range(chunksToLoadX):
        # print('New Chunk Added')
        for y in range(chunkSize):
            for x in range(chunkSize):
                # print('chunk', chunkY, chunkX, 'cell', y, x)
                mapChunks.addCell(chunkX, chunkY)