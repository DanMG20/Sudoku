from algoritmo import SudokuGenerator
class Board: 

    def __init__(self,difficulty):
        self.difficulty = difficulty
        self.board_array = self.get_sudoku()


    def get_sudoku(self): 
        board_array  = SudokuGenerator(self.difficulty)
        return board_array.incomplete_array



tablero_1 = Board("Díficil")

    