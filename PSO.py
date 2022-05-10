import copy
import numpy as np

class Individuo:
    def __init__(self, solucion, velocidad):
        self._solucion = solucion
        self._velocidad = velocidad
        self._b = copy.deepcopy(solucion)
        self._b_fitness = np.inf

class PSO:
    def __init__(self,
    cantidad_individuos,
    dimensiones,
    ro, #Tamaño de vecindad
    phi1_max,
    phi2_max,
    v_max,
    problema,
    generaciones):
        self._cantidad_individuos = cantidad_individuos
        self._dimensiones = dimensiones
        self._ro = ro
        self._phi1_max = phi1_max
        self._phi2_max = phi2_max
        self._v_max = v_max
        self._problema = problema
        self._generaciones = generaciones
        self._individuos = []
        self._rango = self._problema.MAX_VALUE - self._problema.MIN_VALUE
        self._mejor = np.inf

    def crearIndividuos(self):
        for i in range(self._cantidad_individuos):
            solucion = np.random.random(size = self._dimensiones) * self._rango + self._problema.MIN_VALUE
            velocidad = np.random.random(size = self._dimensiones) * self._v_max * 2 + self._v_max
            individuo = Individuo(solucion, velocidad)
            individuo._b_fitness = self._problema.fitness(individuo._solucion)
            self._individuos.append(individuo)

    def mejorIndividuo(self):
        for i in self._individuos:
            fitness = self._problema.fitness(i._solucion)
            if fitness < self._mejor:
                self._mejor = fitness

    def run(self):
        self.crearIndividuos()
        self.mejorIndividuo()
        generaciones = []
        generacion = 0
        while generacion <= self._generaciones:
            for idx in range(len(self._individuos)):
                h = 0
                for i in range(-self._ro // 2, self._ro // 2 + 1):
                    if i == 0:
                        continue
                    elif i == -self._ro // 2:
                        h = copy.deepcopy(self._individuos[(idx + i) % len(self._individuos)])
                    elif self._problema.fitness(self._individuos[(idx + i) % len(self._individuos)]._solucion) < self._problema.fitness(h._solucion):
                        h = copy.deepcopy(self._individuos[(idx + i) % len(self._individuos)])
                phi1 = np.random.random(size = self._dimensiones) * self._phi1_max
                phi2 = np.random.random(size = self._dimensiones) * self._phi2_max
                self._individuos[idx]._velocidad = (self._individuos[idx]._velocidad +
                np.multiply(phi1, self._individuos[idx]._b - self._individuos[idx]._solucion) +
                np.multiply(phi2, h._solucion - self._individuos[idx]._solucion))
                for i in range(self._dimensiones):
                    if abs(self._individuos[idx]._velocidad[i]) > self._v_max:
                        self._individuos[idx]._velocidad[i] = self._v_max / (self._individuos[idx]._velocidad[i])
                self._individuos[idx]._solucion = self._individuos[idx]._solucion + self._individuos[idx]._velocidad
                fitness_individuo = self._problema.fitness(self._individuos[idx]._solucion)
                if fitness_individuo < self._individuos[idx]._b_fitness:
                    self._individuos[idx]._b = copy.deepcopy(self._individuos[idx]._solucion)
                    self._individuos[idx]._b_fitness = fitness_individuo
                    if fitness_individuo < self._mejor:
                        self._problema.fitness(self._individuos[idx]._solucion, True)
                        self._mejor = fitness_individuo
            
            if generacion % 100 == 0:
                print('Generación ', generacion, ':', self._mejor)
                generaciones.append(abs(self._mejor))
            generacion += 1
        
        return generaciones 
