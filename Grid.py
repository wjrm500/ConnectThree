from collections import defaultdict
from typing import List

from Checker import Checker
from Slot import Slot

class Grid:
    def __init__(self, num_rows: int, num_cols: int, winning_score: int = 3) -> None:
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.winning_score = winning_score
        self.grid = [[Slot(row, col) for col in range(num_cols)] for row in range(num_rows)]
        self.slots = [slot for row in self.grid for slot in row]
        self.rows = self.get_rows()
        self.cols = self.get_cols()
        self.diags = self.get_diags()
        self.num_available_slots = num_rows * num_cols
        self.winner = None

    def __str__(self) -> str:
        s = ''
        for row in self.grid:
            s += '| ' + ' | '.join([slot.checker.value for slot in row]) + ' |\n'
        return s.rstrip('\n')
    
    def get_rows(self) -> None:
        rows = defaultdict(list)
        for slot in self.slots:
            rows[slot.row].append(slot)
        return list(rows.values())

    def get_cols(self) -> None:
        cols = defaultdict(list)
        for slot in self.slots:
            cols[slot.col].append(slot)
        return list(cols.values())

    def get_diags(self) -> None:
        diags = defaultdict(list)
        for slot in self.slots:
            diags[slot.diag].append(slot)
        return list(diags.values())
    
    def available_col_idxs(self) -> List[int]:
        return [idx for idx, col in enumerate(self.cols) if col[0].checker == Checker.NULL]
    
    def place_checker(self, col_idx: int, checker: Checker) -> None:
        if col_idx > self.num_cols - 1:
            raise Exception('Col idx is too high')
        if not col_idx in self.available_col_idxs():
            raise Exception('Col idx is not available')

        col = self.cols[col_idx]
        placed = False
        row_idx = -1
        while not placed:
            if col[row_idx].checker == Checker.NULL:
                col[row_idx].checker = checker
                placed = True
            else:
                row_idx -= 1
        self.num_available_slots -= 1
    
    def check_winner_on_line(self, line) -> Checker:
        count = 0
        for i in range(1, len(line)):
            current_slot, previous_slot = line[i], line[i - 1]
            if current_slot.checker == Checker.NULL or current_slot.checker != previous_slot.checker:
                count = 0
            else:
                count += 1
            if count == self.winning_score - 1:
                return current_slot.checker
        return None
    
    def check_winner(self) -> Checker:
        for lines in [self.rows, self.cols, self.diags]:
            for line in lines:
                winner = self.check_winner_on_line(line)
                if winner is not None:
                    return winner
        return None
    
    def game_over(self) -> bool:
        self.winner = self.check_winner()
        return self.num_available_slots == 0 or self.winner is not None