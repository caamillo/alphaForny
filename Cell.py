class Cell:
    def __init__(self, gridX, gridY, size, type = None) -> None:
        self.gridX = gridX
        self.gridY = gridY
        self.posX = gridX * size
        self.posY = gridY * size
        self.type = None
    def print(self):
        print('# ', end='')