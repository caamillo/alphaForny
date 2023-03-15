from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

class Pathfindinder:
    def __init__(self, startX, startY) -> None:
        self.startX = startX
        self.startY = startY
    def createMatrix(self, endX, endY):
        matrix = []

        pathY = range(self.startY, endY) if self.startY < endY else range(endY, self.startY)
        pathX = range(self.startX, endY) if self.startX < endX else range(endX, self.startX)

        for c, y in enumerate(pathY):
            matrix.append([])
            for x in pathX:
                matrix[c].append(1)
        
        return matrix

    def findPath(self, endX, endY):
        matrix = self.createMatrix(endX, endY)
        grid = Grid(matrix = matrix)

        start = grid.node(self.startX, self.startY)
        end = grid.node(endX, endY)

        finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
        path, runs = finder.find_path(start, end, grid)

        return path
# print(grid.grid_str(path=path, start=start, end=end))