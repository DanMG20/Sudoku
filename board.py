from sudoku_generator import SudokuGenerator
from square import Square
import numpy as np
class Board: 

    def __init__(self,difficulty):
        self.difficulty = difficulty
        self.board_array = SudokuGenerator(self.difficulty)
        self.board = []
        self.board_array_map = self.get_sudoku()
        self.gen_board()
        self.selected_pos = None
    def is_sudoku_solved(self):
        
        for row in self.board:
            for square in row: 
                if square.its_hidden:
                    return False
                if square.its_wrong: 
                    return False
        return True


    def is_valid(self,position, box_value):
        row,col = position
                # fila
        for c in range(9):
            if c != col and self.board[row][c].value == box_value:
                return False

        # columna
        for r in range(9):
            if r != row and self.board[r][col].value == box_value:
                return False

        # subcuadro
        box_row = (row // 3) * 3
        box_col = (col // 3) * 3

        for r in range(box_row, box_row + 3):
            for c in range(box_col, box_col + 3):
                if (r, c) != (row, col) and self.board[r][c].value == box_value:
                    return False

        return True

    def get_sudoku(self): 
        return self.board_array.incomplete_array
    
    def gen_board(self): 
        for row in range(9): 
            row_in = []
            for column in range(9): 
                box_value = self.board_array_map[row][column] 
                if box_value == 0: 
                    its_hidden = True
                    its_fixed = False
            
                else:
                    its_hidden = False
                    its_fixed = True
                
                its_wrong = False

                square = Square((row,column),box_value,its_hidden,its_fixed,its_wrong)
                row_in.append(square)
            self.board.append(row_in)


    def get_board(self):
        return self.board

    def manage_click(self, square_pos):
        row_board,col_board = square_pos

        for row in self.board: 
            for square in row:
                square.clicked = False 

        square = self.board[row_board][col_board]
        if not square.its_fixed:
            square.click()
            self.selected_pos = row_board,col_board

    def set_value(self, key_pressed):
        for row in self.board:
            for square in row: 
                
                if square.clicked and not square.its_fixed:

                    if key_pressed == 0:
                        square.value = 0
                        square.its_hidden = True
                        square.its_wrong = False
                        return 
                    
                    if self.is_valid((square.position[0], square.position[1]), key_pressed):
                        square.value = key_pressed
                        square.its_hidden = False
                        square.its_wrong = False

                    else:
                        square.value = key_pressed
                        square.its_hidden = False
                        square.its_wrong = True

    def move_selection(self,dx,dy):
        if self.selected_pos is None: 
            return 
        
        row, col = self.selected_pos 
        new_row = row + dy
        new_col = col + dx

        if  not (0 <= new_row <9 and 0 <= new_col <9):
            return 
        
        next_square = self.board[new_row][new_col]

        if next_square.its_fixed:
            return
        self.board[row][col].clicked = False
        next_square.clicked = True 
        self.selected_pos = (new_row, new_col)
    def reset_board(self):
        for row in self.board:
            for square in row: 
                if not square.its_fixed:
                    square.its_hidden = True
                    square.value = 0 


            


