from problem import FermatsLastTheorem
from DEO import DEO
from result_writer import ResultWriter

def calculo(grado, generaciones):
    dimension = 3                   # Cromosoma de 2 terminos y un exponente (a, b, n)
    cantidad_individuos = 250
    f = 0.6
    c = 0.3
    n_generaciones = generaciones

    problema = FermatsLastTheorem(grado)
    deo = DEO(cantidad_individuos, dimension, f, c, problema, n_generaciones)
    return deo.run() 

def main():
    dimensiones = range(3, 16)
    generaciones = range(0, 1_501, 100)
    n_generaciones = generaciones[-1]
    ejecuciones = 25

    header = ['Dimension', 'a', 'b'] + [f"Generacion {g}" for g in generaciones]
    print(header)

    report = ResultWriter(header)

    for dimension in dimensiones:
        for _ in range(ejecuciones):
            resultados = calculo(dimension, n_generaciones)
            mejor = resultados[-1]['best']
            row = [
                dimension,
                abs(mejor[0]),
                abs(mejor[1])
            ] + [ 
                rec['fitness'] for rec in resultados
            ]
            report.write_record(row)


if __name__ == '__main__':
    main()