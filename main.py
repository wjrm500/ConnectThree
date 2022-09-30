from Checker import Checker
from Grid import Grid

grid = Grid(3, 5)
grid.place_checker(0, Checker.RED)
grid.place_checker(0, Checker.YELLOW)
print(str(grid))