from random import randint
import numpy as np

class Cuadrante: 
    def __init__(self):
        orden= self.generador_orden_aleatorio()
        self.cuadrante = self.generador_cuadrante(orden)

    def __str__(self): 
        return str(self.cuadrante)
    


    def generador_orden_aleatorio(self):
        orden_numeros= []
        while len(orden_numeros) != 9:
            numero_aleatorio = randint(1,9)
            if numero_aleatorio not in orden_numeros:
                orden_numeros.append(numero_aleatorio)
        return orden_numeros

    def generador_cuadrante(self,orden_numeros):
        cuadrante = np.empty((3,3), dtype=int)
        indice=0
        for columna in range(3):
            for fila in range(3): 
                
                cuadrante[columna][fila] = orden_numeros[indice]
                indice +=1
        return cuadrante
 