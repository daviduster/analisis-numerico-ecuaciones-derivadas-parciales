from scipy.linalg import hilbert
import numpy as np
from numpy import linalg as LA

for n in range(2,5):        
    # Create a Hilbert matrix of order n
    h = hilbert(n)
    # Calculate inverse
    h_inv = LA.inv(h)
    print("Matriz de hilbert de orden: " + str(n) +"\n", h)
    print("Matriz inversa de hilbert de orden: " + str(n) +"\n", h_inv)
    # Calculate norm 1
    norm_1 = LA.norm(h, 1)
    norm_1_inv = LA.norm(h_inv, 1)
    print("Norma 1: ", norm_1)
    print("Norma 1 de la inversa: ", norm_1_inv)
    # Calculate condition number using norm 1
    print("Condicionamiento de la matriz en norma 1: ", norm_1*norm_1_inv)
    # Calculate norm 2
    norm_2 = LA.norm(h, 2)
    norm_2_inv = LA.norm(h_inv, 2)
    print("Norma 2: ", norm_2)
    print("Norma 2 de la inversa: ", norm_2_inv)
    # Calculate condition number using norm 2
    print("Condicionamiento de la matriz en norma 2: ", norm_2*norm_2_inv)
    # Calculate norm infinite
    norm_inf = LA.norm(h, np.inf)
    norm_inf_inv = LA.norm(h_inv, np.inf)
    print("Norma infinito: ", norm_inf)
    print("Norma infinito de la inversa: ", norm_inf_inv)
    # Calculate condition number using norm infinite
    print("Condicionamiento de la matriz en norma infinito: ", norm_inf*norm_inf_inv)