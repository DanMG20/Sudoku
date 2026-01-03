from random import shuffle
import numpy as np

class Cuadrante: 
    def __init__(self):
        orden= self.gen_random_order()
        self.cuadrante = self.quadrant_gen(orden)

    def __str__(self): 
        return str(self.cuadrante)
    
    def gen_random_order(self):
        num_order= [n for n in range(1,10)]
        shuffle(num_order)
        return num_order

    def quadrant_gen(self,num_order):
        quadrant = np.zeros((3,3), dtype=int)
        index=0
        for col in range(3):
            for row in range(3): 
                quadrant[row][col] = num_order[index]
                index +=1
        return quadrant
 