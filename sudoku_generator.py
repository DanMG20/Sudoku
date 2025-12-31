from array import array 
import numpy as np
import random
from cuadrante import Cuadrante
import logging
"""

Metodo de generacion 
Funcion de generacion
 1.-Crea 3 cuadrantes en diagonal de manera aleatoria con numeros del 1 al 9 
 2.- Los inserta junto con los 9 cuadrantes del tablero de sudoku 
 3 .- Un algoritmo empieza a generar los numeros faltantes de manera aleatoria pero compliendo
coon las reglas de sudoku 
4.- Se obtiene el tablero de juego completo

Funcion de selección de dificultad
Fácil = Existen 3 maneras iniciales distintas de empezar a solucionar el sudoku 
Medio = Existen 2 maneras iniciales distintas de empezar a solucionar el sudoku
Díficil = Existen 1 maneras iniciales distintas de empezar a solucionar el sudoku

1.- El algoritmo inicia a remover numeros hasta que llegue a la dificultad deseada 
 """ 

logger = logging.getLogger(__name__)
class SudokuGenerator: 

    def __init__(self, difficulty): 
        self.difficulty = difficulty
        self.main_cuadrants = self.gen_diagonal_quadrants()
        
        self.incomplete_array = self.gen_incomplete_main_array()
        self.solve(self.incomplete_array)
        print(self.incomplete_array)
        self.random_pos = self.generate_random_positions()
        self.unsolve(self.random_pos,self.difficulty)
        
        logger.debug("Logica de juego completada") 

        

    def gen_diagonal_quadrants(self):
        logger.debug("Creacion de cuadrantes base iniciada")
        cuadrantes_principales = []
        for indice in range(3):
            cuadrante = Cuadrante()
            cuadrantes_principales.append(cuadrante)
        return cuadrantes_principales
    
    def gen_incomplete_main_array(self):
        logger.debug("Creación del array principal completo iniciada")
        incomplete_array = np.zeros((9,9), dtype = int)

        for num_cuadrante in range(3):
            if num_cuadrante == 0:
                initial_position = (0,0)
                initial_column_position = 0 
            elif num_cuadrante ==1:
                initial_position = (3,3)
                initial_column_position = 3
            else:
                initial_position = (6,6)
                initial_column_position = 6
    
            for row in range(3):
                for column in range(3): 
                    incomplete_array[initial_position[0]][initial_position[1]] = self.main_cuadrants[num_cuadrante].cuadrante[row][column]
                    initial_position = (initial_position[0],initial_position[1]+ 1)
                initial_position = (initial_position[0]+1,initial_column_position)
        return incomplete_array
    
    def find_empty_box(self, array):
        for row_index in range(9):
            for column_index in range(9):
                if array[row_index][column_index] == 0: 
                    return (row_index,column_index)
        return None
    def validate_box(self,row_index,column_index, test_value,array):
        return (
            self.validate_row(row_index,test_value,array) and
            self.validate_column(column_index,test_value,array) and 
            self.validate_quadrant(row_index,column_index,test_value,array)
            )
    

    def validate_row(self,row_index,test_value,array): 
        return test_value not in array[row_index]
    
    def validate_column(self,column_index, test_value,array):
        return test_value not in array[:,column_index]
    
    def validate_quadrant(self, row_index, column_index, test_value,array):
        start_row_quadrant = (row_index // 3) * 3
        start_column_quadrant = (column_index // 3) * 3 

        for row_q in range(3): 
            for column_q in range(3): 
                if array[start_row_quadrant+row_q][start_column_quadrant+column_q] == test_value:
                    return False

        return True 
    
    def solve(self,array):    
        empty_position = self.find_empty_box(array)
        if not empty_position: 
            return True
        
        row_index,column_index = empty_position

        for test_number in range (1,10):
            valid_number = self.validate_box(row_index,column_index,test_number,array)
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
        random.shuffle(random_filled_positions)
        return random_filled_positions


    def unsolve(self,random_filled_positions,difficulty): 
        main_array_copy = self.incomplete_array.copy()
        """
        Facil = 36 pistas, 45 posiciones vacias
        Normal = 32 pistas, 49 posiciones vacias
        Difícil = 28 pistas, 53 posiciones vacias
        """
        difficulty_options = {
            "Fácil": 45,
            "Normal": 49,
            "Difícil": 53}
        
        count = 0
        for pos in random_filled_positions:
            if count <= difficulty_options[difficulty]:
                row,column = pos
                
                self.incomplete_array[row][column] = 0 
                copy_array = self.incomplete_array.copy()
                
                resultado = self.solve(copy_array)
                if resultado:
                    count +=1
                elif not resultado:
                    self.incomplete_array[row][column] = main_array_copy[row][column]

 
