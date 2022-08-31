import numpy as np
import matplotlib.pyplot as plt
from math import pow
from io import StringIO


def main():
    x, y = set_data()
    v = vandermonde_matrix(x, y)
    ix, fix = interpolation_polynomial(v, y)
    graph(x, y, ix, fix)


def set_data():
    # obtener coordenadas de las abscisas
    absc = open("abscisas.txt", "r")
    x = np.array(np.genfromtxt(StringIO(absc.read()), delimiter=","))
    absc.close()
    # obtener coordenadas de las ordenadas
    orde = open("ordenadas.txt", "r")
    y = np.array(np.genfromtxt(StringIO(orde.read()), delimiter=","))
    orde.close()
    
    return x, y


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
    x = np.linspace(-30, 30, num=100) # valores en x para reemplazar
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
    plt.plot(x, y, 'ro', label="puntos")
    plt.plot(ix, fix, label="polinomio", color="green")
    plt.show()


if __name__ == "__main__":
    main()
