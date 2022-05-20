from problem import FermatsLastTheorem
from DEO import DEO

def main():
    dimension = 3                   # Cromosoma de 2 terminos y un exponente (a, b, n)
    cantidad_individuos = 150
    f = 0.6
    c = 0.3
    n_generaciones = 100_000
    dimension_maxima = 3           # Solve for n = 3
    dimension_minima = 3

    problema = FermatsLastTheorem(dimension_maxima, dimension_minima)
    deo = DEO(cantidad_individuos, dimension, f, c, problema, n_generaciones)

    deo.run() 

if __name__ == '__main__':
    main()