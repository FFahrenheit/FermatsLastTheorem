import numpy as np

class FermatsLastTheorem:
    MIN_VALUE = 1                   # Solo numeros enteros positivos
    MAX_VALUE = 2_500_000

    # Se ajusta el rango dependiendo la dimension     
    def __init__(self, dimension) -> None:
        self.dimension = dimension
        self.MAX_VALUE /= (dimension - 2)
    
    """
        a^n + b^n = c^n

        n > 2
        a, b, c ∈ Z - {0}
    """
    def fitness(self, cromosoma, print_console=False) -> float:
        n = self.dimension
        
        # Primeros n-1 elementos, su absoluto en forma de entero 
        values = [ int(abs(round(c)) % self.MAX_VALUE) for c in cromosoma ]    

        # Si los terminos son 0 o estan repetidos 
        if 0 in values or len(values) != len(set(values)):
            return np.inf
        
        # Calculo de la ecuacion
        value_sum = sum([v ** n for v in values])

        # Calculo de la raiz real
        root = np.power(value_sum, (1/n))

        # Si no hay raiz, se descarta
        if np.isnan(root):
            return np.inf

        # Obtenemos la raiz entera
        expected = int(round(root))

        # Si la raiz entera es un elemento (descartamos que los elementos -1, -2, -3 tengan peso)
        for v in values:
            if v == expected:
                return np.inf

        # Calculo de la hipotesis real
        expected_total = expected ** n

        # Diferencia entre la hipotesis y el resultado esperado, multiplicado para ver diferencia en fitness
        difference = abs(expected_total - value_sum)

        # Tasa de precisión, error obtenido, aquí cuentan los pesos de cada número
        accuracy = min([value_sum, expected_total]) / max([value_sum, expected_total])
        
        # accuracy entre [0, 1] -> entre mayor mejor (dividir hace menos fitness)
        # difference entre [0, inf] -> entre menor mejor (multiplicar hace mas fitness)
        fitness = difference/accuracy

        # print(expected)
        if print_console:
            print(f"""
    {' + '.join([str(v) + '^' + str(n) for v in values])} = {value_sum}^(1/{n}) = {expected}^{n}
            """)
            print(f"{values=}\t{value_sum=}\t{expected_total=}\t{difference=}\t{fitness=}\t{accuracy=}")
        
        return fitness


class EulersConjecture:
    MIN_VALUE = 1                   # Solo numeros enteros positivos
    MAX_VALUE = 2_500_000

    # Se ajusta el rango dependiendo la dimension     
    def __init__(self, dimension) -> None:
        self.dimension = dimension
        self.MAX_VALUE /= (dimension - 2)
    
    """
        a^n + b^n = c^n

        n > 2
        a, b, c ∈ Z - {0}
    """
    def fitness(self, cromosoma, print_console=False) -> float:
        n = self.dimension
        
        # Primeros n-1 elementos, su absoluto en forma de entero 
        values = [ int(abs(round(c)) % self.MAX_VALUE) for c in cromosoma ]    
        coef_sum = sum(values)

        # Si los terminos son 0 o estan repetidos 
        if 0 in values or len(values) != len(set(values)):
            return np.inf
        
        # Calculo de la ecuacion
        value_sum = sum([v ** n for v in values])

        # Calculo de la raiz real
        root = np.power(value_sum, (1/n))

        # Si no hay raiz, se descarta
        if np.isnan(root):
            return np.inf

        # Obtenemos la raiz entera
        expected = int(round(root))

        # Si la raiz entera es un elemento (descartamos que los elementos -1, -2, -3 tengan peso)
        for v in values:
            if v == expected:
                return np.inf

        # Calculo de la hipotesis real
        expected_total = expected ** n

        # Diferencia entre la hipotesis y el resultado esperado, multiplicado para ver diferencia en fitness
        difference = abs(expected_total - value_sum)

        # Tasa de precisión, error obtenido, aquí cuentan los pesos de cada número
        accuracy = min([value_sum, expected_total]) / max([value_sum, expected_total])
        
        # accuracy entre [0, 1] -> entre mayor mejor (dividir hace menos fitness)
        # difference entre [0, inf) -> entre menor mejor (multiplicar hace mas fitness)
        # value sum entre (1, inf) -> entre mayor mejor
        fitness = difference / (coef_sum/2)

        # print(expected)
        if print_console:
            print(f"""
    {' + '.join([str(v) + '^' + str(n) for v in values])} = {value_sum}^(1/{n}) = {expected}^{n}
            """)
            print(f"{values=}\t{value_sum=}\t{expected_total=}\t{difference=}\t{fitness=}\t{accuracy=}")
        
        return fitness