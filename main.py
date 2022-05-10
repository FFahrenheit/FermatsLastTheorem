import functions
import DEO
import PSO
import matplotlib.pyplot as plt

def main():
    s = functions.LastFermatTheorem(3)
    dimension = 2
    rango = s.MAX_VALUE - s.MIN_VALUE
    cantidad_individuos = 50
    ro = 8
    phi1_max = 1.7
    phi2_max = 2.0
    v_max = rango * 0.01
    n_generaciones = 2000

    pso = PSO.PSO(cantidad_individuos, dimension, ro, phi1_max, phi2_max, v_max, s, n_generaciones)
    pso.run()

def differential_evolution():
    print('Iniciando algoritmo...')
    dimension = 3
    cantidad_individuos = 100
    f = 0.6
    c = 0.3
    n = 3           #Solve for n = 3
    problema = functions.LastFermatTheorem(n)

    n_generaciones = 100_000

    deo = DEO.DEO(cantidad_individuos, dimension, f, c, problema, n_generaciones)

    deo.run()
    # print(deo)


funciones = [
    functions.Sphere,
    functions.Rosenbrock,
    functions.Rastrigin,
    functions.Quartic
]
dimensiones = [2, 4, 8]
generaciones = [i for i in range(0, 2001, 100)]
numero_ejecuciones = 5
colors = { 2: 'r', 4: 'g', 8: 'b' }

def benchmark():

    for Funcion in funciones:
        promedios = []

        for dimension in dimensiones:
            ejecuciones = []
            for _ in range(numero_ejecuciones):
                cantidad_individuos = 100
                f = 0.6
                c = 0.3
                problema = Funcion()

                n_generaciones = 5000

                deo = DEO.DEO(cantidad_individuos, dimension, f, c, problema, n_generaciones)
                ejecuciones.append(deo.run())

            promedio = get_promedios(ejecuciones)
            promedios.append(promedio)
            
            _, ax = plt.subplots(1)

            ax.plot(generaciones, promedio, colors[dimension])
            
            plt.title(f"{Funcion.__name__} de {dimension} dimensiones")
            # ax.set_ylim(ymin=0)
            plt.show()
        
        _, ax = plt.subplots(1)
        [ plt.plot(generaciones, promedios[index], colors[dimension], 
            label = f"{dimension} Dimensiones") for index, dimension in enumerate(dimensiones)]
        ax.legend(loc='upper right', frameon = False)
        # ax.set_ylim(ymin=0)
        plt.title(f"{Funcion.__name__}")
        plt.show()

def get_promedios(ejecuciones):
    promedios = [0 for _ in range(len(ejecuciones[0]))]
    for i in range(len(ejecuciones[0])):
        for ejecucion in ejecuciones:
            promedios[i] += ejecucion[i]
        promedios[i] /= len(ejecuciones)
    return promedios

if __name__ == '__main__':
    differential_evolution()