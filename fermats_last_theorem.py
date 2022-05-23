import random
import numpy as np
from problem import FermatsLastTheorem
from DEO import DEO
from result_writer import ResultWriter
import matplotlib.pyplot as plt

def calculo(grado, generaciones):
    dimension = 2                           # Cromosoma de 2 terminos (a, b)
    cantidad_individuos = 250
    f = 0.6
    c = 0.3
    n_generaciones = generaciones

    problema = FermatsLastTheorem(grado)
    deo = DEO(cantidad_individuos, dimension, f, c, problema, n_generaciones)
    return deo.run() 

def main():
    dimensiones = range(3, 9)
    generaciones = range(0, 1_501, 100)
    n_generaciones = generaciones[-1]
    ejecuciones = 25
    ngeneraciones = list(generaciones)[-10:]

    header = ['Dimension', 'a', 'b'] + [f"Generacion {g}" for g in generaciones]
    print(header)

    report = ResultWriter(header, 'fermat')

    for dimension in dimensiones:
        coeficientes = []
        
        plt.figure(0)
        plt.title('Fitness over generations')
        plt.xlabel('Generations')
        plt.ylabel('Fitness')

        plt.figure(1)
        plt.title('Fitness over last 1000 generations')
        plt.xlabel('Generations')
        plt.ylabel('Fitness')
        for _ in range(ejecuciones):
            resultados = calculo(dimension, n_generaciones)
            mejor = resultados[-1]['best']
            valores = [int(abs(val)) for val in mejor]
            fitness = [rec['fitness'] for rec in resultados]
            row = [ dimension ] + valores + fitness

            valores = sorted(valores)
            report.write_record(row)
            if valores in coeficientes:
                continue
            coeficientes.append(valores)

            color = [random.random(), random.random(), random.random()]
            root = int(
                round(
                    np.power(
                        sum([a**dimension for a in valores]), 
                        (1/dimension)
                    )
                )
            )
            label = f"{' + '.join([str(v) + '^' + str(dimension) for v in valores])} = {root}^{dimension}"

            plt.figure(0)
            plt.plot(generaciones, fitness, color=color, label=label)
            plt.legend(loc='best')


            plt.figure(1)
            nfitness = fitness[-10:]
            plt.plot(ngeneraciones, nfitness, color=color, label=label)
            plt.legend(loc='best')
            


        plt.show()



if __name__ == '__main__':
    main()