import numpy as np

class LastFermatTheorem:
    MIN_VALUE = -500_000
    MAX_VALUE = 500_000
    
    def __init__(self, n) -> None:
        self.n = n
        self.multiply_factor = 10_000
    
    def fitness(self, cromosoma, print_console=False):
        values = [ round(c) for c in cromosoma ]

        if 0 in values:
            return np.inf
        
        value_sum = 0
        for v in values:
            value_sum += v ** self.n

        root = np.power(value_sum, (1/self.n))
        if np.isnan(root) or round(root) == 0:
            return np.inf

        expected = round(root)

        for v in values:
            if v == expected:
                return np.inf 

        # print(expected)
        if print_console:
            print(expected)
            print(f"""
            {' + '.join([str(v) + '^3' for v in values])} = {value_sum}^(1/3) = {expected}^3
            """)
            print(f"{values}\t{value_sum}\t{root}\t{expected}\t{abs(expected ** self.n - value_sum)}")
        
        return abs(expected ** self.n - value_sum) - (sum([abs(v) for v in values]))/( self.MAX_VALUE*self.n )
        

class Sphere:
    MIN_VALUE = -5.12
    MAX_VALUE = 5.12
    def __init__(self):
        pass
    def fitness(self, cromosoma):
        z = 0
        for alelo in cromosoma:
            z += alelo**2
        return z

class Rosenbrock:
    MIN_VALUE = -2.048
    MAX_VALUE = 2.048
    def __init__(self):
        pass
    def fitness(self, cromosoma):
        z = 0
        x = cromosoma       #Alias
        for i in range(len(cromosoma) - 1):
            z += 100 * (x[i+1] - x[i]**2) ** 2 + (x[i] - 1)**2
        return z

class Rastrigin:
    MIN_VALUE = -5.12
    MAX_VALUE = 5.12
    def __init__(self):
        pass
    def fitness(self, cromosoma, A = 10):
        z = A * len(cromosoma)
        for alelo in cromosoma:
            z += alelo**2 - A * np.cos(2 * np.pi * alelo)
        return z

class Quartic:
    MIN_VALUE = -1.28
    MAX_VALUE = 1.28
    def __init__(self):
        pass
    def fitness(self, cromosoma):
        z = 0
        for alelo in cromosoma:
            z += alelo**4
        return z