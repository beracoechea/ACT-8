# algoritmos.py
import math
def distancia_euclidiana(x_1, y_1, x_2, y_2):
    
    aux1 =  x_2-x_1
    aux1 = aux1*aux1
    aux2 = y_2-y_1
    aux2 = aux2*aux2
    distancia = math.sqrt(aux1+aux2)
    
    return (distancia)