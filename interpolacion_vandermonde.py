import numpy as np
import matplotlib.pyplot as plt
from math import pow


def main():
    x = np.array([0,1,2])
    y = np.array([2,3,2])
    v = vandermonde_matrix(x, y)
    ix, fix = interpolation_polynomial(v, y)
    graph(x, y, ix, fix)


def vandermonde_matrix(x, y):
    # Construccion de la matriz de vandermonde
    vandermonde = []
    for i in x:
        column = []
        for j in range(x.size):
            column.append(pow(i, j))
        vandermonde.append(column)
        
    return np.matrix(vandermonde)

def interpolation_polynomial(v, y):
    a = np.linalg.solve(v, y) # Conjunto de soluciones
    x = np.linspace(0, 2, num=100) # valores en x para reemplazar
    pol = [] # polinomio
    for j in range(a.size):
        pol.append(a[j]*x**j)
    fx = np.array(sum(pol)) # Array con los valores que toma f(x)

    return x, fx

def graph(x, y, ix, fix):
    # Puntos dados
    plt.title('Interpolacion de Vandermonde')
    plt.xlabel('x')
    plt.ylabel('y')
    # Polinomio interpolante
    plt.plot(x, y, 'bo', label="puntos")
    plt.plot(ix, fix, label="polinomio", color="red")
    plt.show()


if __name__ == "__main__":
    main()
