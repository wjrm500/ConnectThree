from typing import List
from Slot import Slot


class Grid:
    def __init__(self) -> None:
        self.num_rows = 3
        self.num_cols = 5
        self.grid = [[Slot.EMPTY for _ in range(self.num_cols)] for _ in range(self.num_rows)]

    def __str__(self) -> str:
        s = ''
        for row in self.grid:
            s += '| ' + ' | '.join([slot.value for slot in row]) + ' |\n'
        return s.rstrip('\n')
    
    def inverted_grid(self):
        inverted_grid = [[] for _ in range(self.num_cols)]
        for row in self.grid:
            for idx, slot in enumerate(row):
                inverted_grid[idx].append(slot)
        return inverted_grid