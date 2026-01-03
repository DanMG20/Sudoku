import numpy as np 
from random import shuffle

class SudokuGenerator:
    """
    It Generates a sudoku array that is possible to solve in function on 
    the difficulty choosed by user.
    The three difficulty options allowed: 
        Easy = 36 clues, 45 empty squares
        Normal = 32 clues, 49 empty squares
        Hard = 28 clues, 53 empty squares

    """

    def __init__(self, difficulty): 
        self.difficulty = difficulty
        self.difficulty_options = {
            "Fácil": 45,
            "Normal": 49,
            "Difícil": 53}
        self.main_cuadrants = self.gen_diagonal_quadrants()
        self.sudoku_array = self.gen_sudoku_array()
        self.solve(self.sudoku_array)
        self.random_pos = self.generate_random_positions()
        self.unsolve(self.random_pos,difficulty)
   
    def gen_random_order(self):
        """
        Generates random order for a quadrant
        """
        num_order= [n for n in range(1,10)]
        shuffle(num_order)
        return num_order

    def quadrant_gen(self,num_order):
        """
        Generates a quadrant with random order.
        
        :param num_order: Gets a list of random ordered numbers from 1 to 9
        """
        quadrant = np.zeros((3,3), dtype=int)
        index=0
        for col in range(3):
            for row in range(3): 
                quadrant[row][col] = num_order[index]
                index +=1
        return quadrant
        

    def gen_diagonal_quadrants(self):
        """
        Generates the three initial random diagonal quadrants for sudoku.
        """
        diagonal_quadrants = []
        for quad in range(3):
            quad =  self.quadrant_gen(self.gen_random_order())
            diagonal_quadrants.append(quad)
        return diagonal_quadrants
    
    def gen_sudoku_array(self):
        """
        It Generates the main array of zeros and replace the diagonal quadrants,
        with the ones created random.

        """
        sudoku_array = np.zeros((9,9), dtype = int)

        for q_index, quadrant in enumerate(self.main_cuadrants):
            base_row = (q_index // 3 ) * 3 
            base_col = (q_index % 3 ) * 3 

            for row in range(3):
                for col in range(3):
                    sudoku_array[base_row + row , base_col + col] = quadrant[row][col]

        return sudoku_array
    
    def find_empty_square(self, array):
        for row in range(9):
            for column in range(9):
                if array[row][column] == 0: 
                    return (row,column)
        return None
    
    def validate_row(self,
                     row,
                     test_value,
                     array): 
        return test_value not in array[row]
    
    def validate_column(self,
                        col, 
                        test_value,array):
        return test_value not in array[:,col]
    
    def validate_quadrant(self, 
                          row, 
                          column, 
                          test_value,array):
        start_row_quadrant = (row // 3) * 3
        start_column_quadrant = (column // 3) * 3 
        
        for row_q in range(3): 
            for column_q in range(3): 
                if array[start_row_quadrant+row_q][start_column_quadrant+column_q] == test_value:
                    return False

        return True 
    

    def validate_square(self,
                        row,
                        column, 
                        test_value,array):
        return (
            self.validate_row(row,test_value,array) and
            self.validate_column(column,test_value,array) and 
            self.validate_quadrant(row,column,test_value,array)
            )
    
    def solve(self,array):    
        """
        It solves an incomplete array with sudoku rules using recursion
        and backtraking

        :param array: It gets the array you want to solve
        """
        empty_position = self.find_empty_square(array)
        if not empty_position: 
            return True
        
        row_index,column_index = empty_position

        for test_number in range (1,10):
            valid_number = self.validate_square(row_index,column_index,test_number,array)
            if valid_number:
                array[row_index][column_index] = test_number
                if self.solve(array): 
                    return True
                array[row_index][column_index] = 0    
        return False
    


    def generate_random_positions(self): 
        random_filled_positions= []
        for i in range(9):
            for j in range(9): 
                position = (i,j)
                random_filled_positions.append(position)
        shuffle(random_filled_positions)
        return random_filled_positions


    def unsolve(self,random_filled_positions,difficulty): 
        """
        It takes the sudoku array and unsolves but by checking that solving again is possible,
        depending on difficulty.
             
        :param random_filled_positions: Random square positions to start unsolving
        :param difficulty: Difficulty choosed by user
        """

        sudoku_solved_copy = self.sudoku_array.copy()
      
        count = 0

        for pos in random_filled_positions:
            if count <= self.difficulty_options[difficulty]:
                row,column = pos
                self.sudoku_array[row][column] = 0 
                copy_array = self.sudoku_array.copy()
                result = self.solve(copy_array)

                if result:
                    count +=1

                elif not result:
                    self.sudoku_array[row][column] = sudoku_solved_copy[row][column]

    
