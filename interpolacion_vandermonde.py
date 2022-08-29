import numpy as np
import matplotlib.pyplot as plt
from math import pow


def main():
    x = np.array([0,1,2])
    y = np.array([2,3,2])
    v = vandermonde_matrix(x, y)
    a = np.linalg.solve(v, y)
    graph(x, y)


def vandermonde_matrix(x, y):
    vandermonde = []
    for i in x:
        column = []
        for j in range(x.size):
            column.append(pow(i, j))
        vandermonde.append(column)
        
    return np.matrix(vandermonde)


def graph(x, y):
    plt.plot(x, y, 'o', label="puntos")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Interpolacion de Vandermonde')
    plt.show()


if __name__ == "__main__":
    main()
