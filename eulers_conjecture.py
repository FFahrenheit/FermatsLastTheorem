import problem
import DEO
from result_writer import ResultWriter

last_fitness = 0
times = 0

def deo_callback(generation, best, best_fitness):
    global times, last_fitness
    record = [ generation ] + list(best) + [ best_fitness ]
    report.write_record(record)

    if last_fitness == best_fitness:
        times += 1
        if times >= 100:
            return True
    else:
        times = 0
        last_fitness = best_fitness

    return False

def differential_evolution():
    global report
    print('Iniciando algoritmo...')
    dimension = 4
    cantidad_individuos = 250
    f = 0.6
    c = 0.3
    n = 5          #Solve for n = 5
    problema = problem.EulersConjecture(n)

    n_generaciones = 100_000

    for i in range(100):
        header = ['generacion', 'a', 'b', 'c', 'd', 'fitness']
        report = ResultWriter(header, f"eulers-conjecture({i})")
        deo = DEO.DEO(cantidad_individuos, dimension, f, c, problema, n_generaciones, deo_callback)
        deo.run()
    # print(deo)

if __name__ == '__main__':
    differential_evolution()