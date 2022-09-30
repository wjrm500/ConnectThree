from typing import List
from Checker import Checker

class Grid:
    def __init__(self, num_rows: int, num_cols: int, winning_score: int = 3) -> None:
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.winning_score = winning_score
        self.grid = [[Checker.NULL for _ in range(num_cols)] for _ in range(num_rows)]
        self.num_available_slots = num_rows * num_cols
        self.winner = None

    def __str__(self) -> str:
        s = ''
        for row in self.grid:
            s += '| ' + ' | '.join([slot.value for slot in row]) + ' |\n'
        return s.rstrip('\n')
    
    def invert_grid(self, grid: List) -> List:
        return list(map(list, zip(*grid)))
    
    def available_col_idxs(self) -> List[int]:
        inverted_grid = self.invert_grid(self.grid)
        return [idx for idx, col in enumerate(inverted_grid) if col[0] == Checker.NULL]
    
    def place_checker(self, col_idx: int, checker: Checker) -> None:
        if col_idx > self.num_cols - 1:
            raise Exception('Col idx is too high')
        if not col_idx in self.available_col_idxs():
            raise Exception('Col idx is not available')
        inverted_grid = self.invert_grid(self.grid)
        placed, row_idx = False, -1
        while not placed:
            if inverted_grid[col_idx][row_idx] == Checker.NULL:
                inverted_grid[col_idx][row_idx] = checker
                placed = True
            else:
                row_idx -=1
        self.grid = self.invert_grid(inverted_grid)
        self.num_available_slots -= 1
    
    def check_winner(self) -> Checker:
        for row in self.grid:
            count = 0
            for i in range(1, len(row)):
                current_slot, previous_slot = row[i], row[i - 1]
                if current_slot == Checker.NULL or current_slot != previous_slot:
                    count = 0
                else:
                    count += 1
                if count == self.winning_score - 1:
                    return current_slot
        return None
    
    def game_over(self) -> bool:
        self.winner = self.check_winner()
        return self.num_available_slots == 0 or self.winner is not None