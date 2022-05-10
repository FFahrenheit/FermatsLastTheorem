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
        