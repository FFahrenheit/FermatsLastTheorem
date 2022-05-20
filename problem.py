from black import diff
import numpy as np

class FermatsLastTheorem:
    MIN_VALUE = 1                   #Solo numeros enteros
    MAX_VALUE = 2_500_000

    # Para min_dimension >= n >= max_dimension
    # Se ajusta el rango dependiendo las maximas dimensiones     
    def __init__(self, max_dimension, min_dimension = 3) -> None:
        self.max_dimension = max_dimension
        self.min_dimension = min_dimension
        self.MAX_VALUE /= (max_dimension - 2)
    
    """
        a^n + b^n = c^n

        n > 2
        a, b, c ∈ Z - {0}
    """
    def fitness(self, cromosoma, print_console=False) -> float:
        # Para obtener 2 > n > max_dimension
        n = int(cromosoma[-1]) % (self.max_dimension - self.min_dimension - 1) + self.min_dimension 
        
        # Primeros n-1 elementos, su absoluto en forma de entero 
        values = [ int(abs(round(c))) for c in cromosoma[:-1] ]    

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

        # Diferencia entre la hipotesis y el resultado esperado
        difference = abs(expected_total - value_sum)

        # Calculo de la suma de elementos para darle peso a la funcion fitness
        elements_totals = sum(values)
        min_value = min(values)
        
        # Calculo final del fitness
        fitness =  difference - elements_totals * min_value / self.MAX_VALUE
        
        # print(expected)
        if print_console:
            print(f"""
    {' + '.join([str(v) + '^' + str(n) for v in values])} = {value_sum}^(1/{n}) = {expected}^{n}
            """)
            print(f"{values}\t{value_sum}\t{expected}\t{difference}\t{fitness}")
        
        return fitness
