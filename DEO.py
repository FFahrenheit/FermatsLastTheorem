import copy
import numpy as np

class DEO:

    def __init__(self,
                individuals_count,
                dimensions,
                stepsize,
                crossover_rate,
                problem,
                generation_count):
        self.individuals_count = individuals_count
        self.dimensions = dimensions
        self.stepsize = stepsize,
        self.crossover_rate = crossover_rate
        self.problem = problem
        self.generation_count = generation_count

    def run(self):
        self.individuals = np.array([ np.random.random_integers(self.problem.MIN_VALUE, self.problem.MAX_VALUE, size = self.dimensions) 
            for _ in range(self.individuals_count) ])
        
        generations = []
        generation = 0

        best = self.individuals[0]
        best_fitness = self.problem.fitness(best)
        
        while generation <= self.generation_count:
            u = []
            v = []
            for i in range(self.individuals_count):
                r1 = self.randint_excluding([i])
                r2 = self.randint_excluding([i, r1])
                r3 = self.randint_excluding([i, r1, r2])

                v.append( 
                    self.individuals[r1] + self.stepsize * (self.individuals[r2] - self.individuals[r3])
                )
                
                tr = np.random.randint(0, self.dimensions)

                u_vector = []
                for j in range(self.dimensions):
                    rcj = np.random.random()

                    if rcj < self.crossover_rate or j == tr:
                        u_vector.append(v[i][j])
                    else:
                        u_vector.append(self.individuals[i][j])

                u.append(u_vector)


            for i in range(self.individuals_count):
                if self.problem.fitness(u[i]) < self.problem.fitness(self.individuals[i]):
                    self.individuals[i] = copy.deepcopy(u[i])
                
                if self.problem.fitness(self.individuals[i]) < best_fitness:
                    best = copy.deepcopy(self.individuals[i])
                    best_fitness = self.problem.fitness(best, True)

            if generation % 100 == 0:
                print(f"Generation {generation}: {best} = {best_fitness}")
                generations.append(
                    (best, best_fitness)
                )
            generation += 1
        
        return generations

    def randint_excluding(self, used):
        rand = np.random.randint(0, self.individuals_count)
        while rand in used:
            rand = np.random.randint(0, self.individuals_count)
        return rand