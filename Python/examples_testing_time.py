
import numpy as np
import time


# Crear funciones a comparar
def superposition1(l1, l2):
    lx = []
    for e1 in l1:
        for e2 in l2:
            if e1 == e2:
                lx.append(e1)
    return lx

def superposition2(l1, l2):
    lx = []
    for e1 in l1:
        if e1 in l2:
            lx.append(e1)
    return lx

# parametros de test
n_pos = 50000000 # numero posible de integers 
n_len = 100000  # longitud de las listas

# Crear listas random para 
l1 = np.random.random_integers(0, n_pos, n_len)
l2 = np.random.random_integers(0, n_pos, n_len)
l1, l2 = list(l1), list(l2)


## Comparar en tiempo
t0 = time.time()
l = superposition1(l1, l2)
print time.time()-t0


t0 = time.time()
l = superposition2(l1, l2)
print time.time()-t0

