import problem
import DEO

def differential_evolution():
    print('Iniciando algoritmo...')
    dimension = 4
    cantidad_individuos = 250
    f = 0.6
    c = 0.3
    n = 5          #Solve for n = 5
    problema = problem.EulersConjecture(n)

    n_generaciones = 100_000

    deo = DEO.DEO(cantidad_individuos, dimension, f, c, problema, n_generaciones)

    deo.run()
    # print(deo)

if __name__ == '__main__':
    differential_evolution()