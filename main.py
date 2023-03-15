from Map import Map
from Cell import Cell

from Pathfinder import Pathfindinder

import cv2 as cv
import numpy as np
import math

frame = cv.imread('pokemmo.png')
h, w, channels = frame.shape

cellSize = int((64 *  w) / 1920) # More Accurate: 64
print('cellSize', cellSize)
chunkSize = 5

margin = 0

# Round nSize to multiple of Chunks Size
nRows = math.ceil(math.ceil(h / cellSize) / chunkSize)
nCols = math.ceil(math.ceil(w / cellSize) / chunkSize)

# Make Rows / Cols in Odd
nRows = nRows * chunkSize if nRows % 2 != 0 else (nRows + 1) * chunkSize
nCols = nCols * chunkSize if nCols % 2 != 0 else (nCols + 1) * chunkSize

# Create Chunks
chunksToLoadX = int(nCols / chunkSize)
chunksToLoadY = int(nRows / chunkSize)

mapChunks = Map(chunksToLoadX, chunksToLoadY, chunkSize)

print('Rows, Cols', nRows, nCols)

rangeCols = math.floor(chunksToLoadX / 2)
rangeRows = math.floor(chunksToLoadY / 2)

for y in range(-rangeRows, rangeRows + 1):
    for x in range(-rangeCols, rangeCols + 1):
        mapChunks.addCell(Cell(x, y, cellSize))

def match_all(image, template, debug=False, color=(0, 0, 255)):
    height, width = template.shape[:2]
    matchProbability = cv.matchTemplate(image, template, cv.TM_CCOEFF_NORMED)
    maxProb = np.max(matchProbability)
    matchLocations = np.where(matchProbability == maxProb)

    locations = []
    for x, y in zip(*matchLocations[::-1]):
        locations.append(((x, x + width), (y, y + height)))

        if debug:
            # print('ciaone', x, y)
            cv.rectangle(image, (x, y), (x + width, y + height), color, 3)
    return locations[0], maxProb
    

((anchor1X, anchor2X), (anchor1Y, anchor2Y)), prob = match_all(frame, cv.imread('shadow.png'), True)

# print((anchor1X, anchor1Y), (anchor2X, anchor2Y))

# cv.rectangle(frame, (anchor1X, anchor1Y), (anchor1X + 30, anchor1Y + 30), (255, 0, 0), 3)

anchorX = anchor1X + math.floor((anchor2X - anchor1X) / 2)
anchorY = anchor1Y + math.floor((anchor2Y - anchor1Y) / 2)

# midCell = mapChunks.getMidChunk().getMidCell()
midCell = mapChunks.getCell(0, 0)

midCellCenterX = midCell.posX + math.ceil(cellSize / 2)
midCellCenterY = midCell.posY + math.ceil(cellSize / 2)

# print('anchors', anchorX, anchorY)
# print('mid', midCellCenterX, midCellCenterY)

offsetX = anchorX - midCellCenterX
offsetY = anchorY - midCellCenterY
# cv.rectangle(frame, (midCellCenterX + offsetX, midCellCenterY + offsetY), (midCellCenterX + 32 + offsetX, midCellCenterY + 32 + offsetY), (0, 0, 255), 3)

# print(offsetX, offsetY)
for y in range(-rangeRows, rangeRows + 1):
    for x in range(-rangeCols, rangeCols + 1):
        print('x y', x, y)
        cell = mapChunks.getCell(x, y)
        print('cell', cell)
        vert1X = (cell.posX) + margin + offsetX
        vert1Y = (cell.posY) + margin + offsetY
        vert2X = (vert1X + cellSize) - margin
        vert2Y = (vert1Y + cellSize) - margin
        if not (cell.gridX == 0 and cell.gridY == 0):
            cv.rectangle(frame, (vert1X, vert1Y), (vert2X, vert2Y), (0, 255, 0), 3)

# Draw Mid
cv.rectangle(frame, (midCell.posX + offsetX, midCell.posY + offsetY), ((midCell.posX + cellSize) + offsetX, (midCell.posY + cellSize) + offsetY), (255, 0, 0), 3)

# Not pixels, but cells
# pathFinder = Pathfindinder(0, 0)
# print(pathFinder.findPath(6, 6))

cv.imshow('Demo', frame)

cv.waitKey(0)
cv.destroyAllWindows()