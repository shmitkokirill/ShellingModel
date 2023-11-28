import random

class Color:
    BLUE    = 1
    RED     = 2
    EMPTY   = 0

class ColUnit:
    def __init__(self, val : any, ratio : float = 0.0, total_cells : int = 0):
        self.value = val
        self.ratio = ratio
        self.count = int(total_cells * ratio)
        self.x = 0
        self.y = 0

class ShellingModel:
    def __init__(self, size: int):
        self.__n = size

        self.__total_cells = self.__n * self.__n

        # colors 
        self.__colors = {
            Color.BLUE:     ColUnit(Color.BLUE, 0.45, self.__total_cells), 
            Color.RED:      ColUnit(Color.RED, 0.45, self.__total_cells),
            Color.EMPTY:    ColUnit(Color.EMPTY, 0.1, self.__total_cells)
        }

        self.__grid = []
        self.__defaultInitGrid()

    def print(self) -> None:
        for row in self.__grid:
            for col_unit in row:
                print(col_unit.value, end=' ')
            print()


    def __fillInSingle(self, col_unit : ColUnit):
        for _ in range(col_unit.count):
            while True:
                x = random.randint(0, self.__n - 1)
                y = random.randint(0, self.__n - 1)
                g = self.__grid[x][y]
                if g.value == self.__colors[Color.EMPTY].value:
                    col_unit.x = g.x
                    col_unit.y = g.y
                    self.__grid[x][y] = col_unit
                    break

    def __defaultInitGrid(self) -> None:
        # fill in with ColUnit.values
        for i in range(self.__n):
            row = []
            for j in range(self.__n):
                col_unit = self.__colors[Color.EMPTY]
                col_unit.x = i
                col_unit.y = j
                row.append(col_unit)
            self.__grid.append(row)
        
        for color, col_unit in self.__colors.items():
            self.__fillInSingle(col_unit)
