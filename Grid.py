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
    
    def invert_grid(self, grid: List) -> List:
        return list(map(list, zip(*grid)))
    
    def available_cols(self) -> List[int]:
        inverted_grid = self.invert_grid(self.grid)
        return [idx for idx, col in enumerate(inverted_grid) if col[0] == Slot.EMPTY]