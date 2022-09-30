import random
from Checker import Checker
from Grid import Grid

grid = Grid(3, 5)

checkers = [Checker.RED, Checker.YELLOW]
swap = lambda c: Checker.YELLOW if c == Checker.RED else Checker.RED
checker = checkers[0]
while not grid.game_over():
    col_idx = random.choice(grid.available_col_idxs())
    grid.place_checker(col_idx, checker)
    checker = swap(checker)
    print(str(grid))
    print('\n')