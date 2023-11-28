import random
from copy import copy

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
        self.is_happy = False

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
        self.__empty_cells = []
        self.__unhappy_cells = []
        self.__defaultInitGrid()

    def print(self) -> None:
        for row in self.__grid:
            for col_unit in row:
                print(col_unit.value, end=' ')
            print()

    def printCoords(self):
        for row in self.__grid:
            for col_unit in row:
                print('{' + str(col_unit.x) + ',' + str(col_unit.y) + '}', end=' ')
            print()


    def printUnhappy(self) -> None:
        for col_unit in self.__unhappy_cells:
            print('{' + str(col_unit.x) + ',' + str(col_unit.y) + '}', end=' ')

    def __collectUnhappyCells(self):
        grid = self.__grid
        for i in range(len(grid)):
            # for each cell
            for j in range(len(grid[i])):
                cell = grid[i][j]

                same_color_neighbors = 0
                # check around current cell
                for x in range(max(0, i - 1), min(i + 2, len(grid))):
                    for y in range(max(0, j - 1), min(j + 2, len(grid[i]))):
                        if (x, y) != (i, j) and grid[x][y].value == cell.value:
                            same_color_neighbors += 1

                if same_color_neighbors < 2:
                    self.__unhappy_cells.append(cell)

    def __fillInSingle(self, col_unit : ColUnit):
        for _ in range(col_unit.count):
            c_cpy = copy(col_unit)
            while True:
                x = random.randint(0, self.__n - 1)
                y = random.randint(0, self.__n - 1)
                g = self.__grid[x][y]
                if g.value == self.__colors[Color.EMPTY].value:
                    c_cpy.x = g.x
                    c_cpy.y = g.y
                    self.__grid[x][y] = c_cpy
                    break

    def __defaultInitGrid(self) -> None:
        # fill in with ColUnit.values
        for i in range(self.__n):
            row = []
            for j in range(self.__n):
                col_unit = copy(self.__colors[Color.EMPTY])
                col_unit.x = i
                col_unit.y = j
                row.append(col_unit)
            self.__grid.append(row)
        
        for color, col_unit in self.__colors.items():
            self.__fillInSingle(col_unit)
        
        self.__collectUnhappyCells()
