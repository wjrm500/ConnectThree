from Checker import Checker


class Slot:
    def __init__(self, row: int, col: int) -> None:
        self.row = row
        self.col = col
        self.diag = row - col
        self.checker = Checker.NULL