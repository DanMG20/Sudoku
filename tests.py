import numpy as np
from cuadrante import Cuadrante
from random import randint
class Algoritmo:

    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.board = np.zeros((9, 9), dtype=int)

        #self.gen_diagonal_quadrants()
        #self.solve()
        random_num = randint(1,9)
        for row in range(9):
            for column in range(9): 
                self.valid_quadrant(row,column, random_num)

        print(self.board)

    # =========================
    # GENERACIÓN
    # =========================
    def gen_diagonal_quadrants(self):
        positions = [(0, 0), (3, 3), (6, 6)]

        for start_row, start_col in positions:
            quad = Cuadrante().cuadrante
            for i in range(3):
                for j in range(3):
                    self.board[start_row + i][start_col + j] = quad[i][j]

    # =========================
    # BACKTRACKING
    # =========================
    def solve(self):
        empty = self.find_empty()
        if not empty:
            return True  # Sudoku resuelto

        row, col = empty

        for num in range(1, 10):
            if self.is_valid(row, col, num):
                self.board[row][col] = num

                if self.solve():
                    return True

                # BACKTRACK
                self.board[row][col] = 0

        return False

    # =========================
    # VALIDACIONES
    # =========================
    def is_valid(self, row, col, num):
        return (
            self.valid_row(row, num) and
            self.valid_col(col, num) and
            self.valid_quadrant(row, col, num)
        )

    def valid_row(self, row, num):
        return num not in self.board[row]

    def valid_col(self, col, num):
        return num not in self.board[:, col]

    def valid_quadrant(self, row, col, num):

        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        print (row//3)
        print(col//3)
        print(f" start_row: { start_row} ; start_column: {start_col}")
        

        for i in range(3):
            for j in range(3):
                if self.board[start_row + i][start_col + j] == num:
                    return False
        return True

    # =========================
    # UTILIDADES
    # =========================
    def find_empty(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    return (row, col)
        return None


alg = Algoritmo("Díficil")