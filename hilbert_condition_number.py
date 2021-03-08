from scipy.linalg import hilbert
import numpy as np
from numpy import linalg as LA

for n in range(2,6):        
    # Create a Hilbert matrix of order n
    h = hilbert(n)
    # Calculate inverse
    h_inv = LA.inv(h)
    print("Matriz de hilbert de orden: " + str(n) +"\n", h)
    # Calculate condition number using norm 1
    print("Condicionamiento de la matriz en norma 1: ", LA.cond(h, 1))
    # Calculate condition number using norm 2
    print("Condicionamiento de la matriz en norma 2: ", LA.cond(h, 2))
    # Calculate condition number using norm infinite
    print("Condicionamiento de la matriz en norma infinite: ", LA.cond(h, np.inf))