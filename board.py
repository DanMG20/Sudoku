from sudoku_generator import SudokuGenerator
from square import Square
class Board: 

    def __init__(self,difficulty):
        self.difficulty = difficulty
        self.sudoku_gen = SudokuGenerator(self.difficulty)
        self.board_array_map = self.sudoku_gen.sudoku_array
        self.board = []
        self.gen_board()
        self.selected_pos = None
    
    def is_sudoku_solved(self):
        for row in self.board:
            for square in row: 
                if square.hidden:
                    return False
                if square.wrong: 
                    return False
        return True


    def is_valid(self,position, value_inserted):
        row,col = position
        return (
        self.is_valid_in_row(row,col,value_inserted) and
        self.is_valid_in_column(row,col, value_inserted) and
        self.is_valid_in_quadrant(row,col, value_inserted)
        )
        
        
    def is_valid_in_row(self,row,col, value_inserted):
        for c in range(9):
            if c != col and self.board[row][c].value == value_inserted:
                return False
        return True
            
    def is_valid_in_column(self,row,col,value_inserted):
        for r in range(9):
            if r != row and self.board[r][col].value == value_inserted:
                return False
        return True
        
    def is_valid_in_quadrant(self, row , col , value_inserted):
        square_row = (row // 3) * 3
        square_col = (col // 3) * 3

        for r in range(square_row, square_row + 3):
            for c in range(square_col, square_col + 3):
                if (r, c) != (row, col) and self.board[r][c].value == value_inserted:
                    return False
        return True
    
    def gen_board(self): 
        for row in range(9): 
            row_in = []
            for column in range(9): 
                square_value = self.board_array_map[row][column] 
                if square_value == 0: 
                    hidden = True
                    fixed = False
                else:
                    hidden = False
                    fixed = True
                
                its_wrong = False

                square = Square((row,column),square_value,hidden,fixed,its_wrong)
                row_in.append(square)
            self.board.append(row_in)

    def get_board(self):
        return self.board

    def clean_selection(self):
        for row in self.board: 
            for square in row:
                square.selected = False 

    def select_square(self, square_pos):
        self.clean_selection()
        row_board,col_board = square_pos
        
        square = self.board[row_board][col_board]
        if not square.fixed:
            square.select()
            self.selected_pos = row_board,col_board

    def set_value(self, key_pressed):
        if self.selected_pos == None: 
                return
        row, col = self.selected_pos
        square = self.board[row][col]

        if square.fixed: 
            return 
        
        if key_pressed == 0:
            square.set_value(0)
            square.hide()
            square.set_not_wrong()
            return 
        
        elif self.is_valid((square.position[0], square.position[1]), key_pressed):
            square.set_value(key_pressed)
            square.unhide()
            square.set_not_wrong()
        else:
            square.set_value(key_pressed)
            square.unhide()
            square.set_wrong()

    def move_selection(self,dx,dy):
        if self.selected_pos is None: 
            return 

        row, col = self.selected_pos 
        new_row = row + dy
        new_col = col + dx

        if  not (0 <= new_row <9 and 0 <= new_col <9):
            return 
        
        next_square = self.board[new_row][new_col]

        if next_square.fixed:
            return
        
        self.board[row][col].selected = False
        next_square.selected = True 
        self.selected_pos = (new_row, new_col)

    def reset_board(self):
        for row in self.board:
            for square in row: 
                if not square.fixed:
                    square.hidde()
                    square.set_value(0)
                    square.set_not_wrong()


            


