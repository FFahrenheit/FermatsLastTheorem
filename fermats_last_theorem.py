from problem import FermatsLastTheorem
from DEO import DEO

def calculo(dimension):
    dimension = 3                   # Cromosoma de 2 terminos y un exponente (a, b, n)
    cantidad_individuos = 100
    f = 0.6
    c = 0.3
    n_generaciones = 100_000

    problema = FermatsLastTheorem(dimension)
    deo = DEO(cantidad_individuos, dimension, f, c, problema, n_generaciones)
    resultados = deo.run() 

def main():
    calculo(3)

if __name__ == '__main__':
    main()