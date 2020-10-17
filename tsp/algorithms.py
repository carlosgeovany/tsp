import numpy as np
import copy

from abc import ABC, abstractmethod

class Algorithm(ABC):

    @abstractmethod
    def run(self, problem, *args):
        pass

class GreedyTSP(Algorithm):
    def __init__(self):
        pass

    def run(self, tsp, start):
        """
        Selecciona los siguientes nodos a visitar de manera greedy
        """
        current = start
        path = [start]
        cost = 0.0

        local_distances = copy.deepcopy(tsp.distances)

        while len(path) < len(tsp.places):
            distances_to = np.copy(local_distances[current,:])
            distances_to[path] = np.infty

            current = np.argmin(distances_to)
            path.append(current)
            cost += np.min(distances_to)
            print(path, cost, current)

        return {'cost': cost, 'path': path}

class Ant:
    """
    Representa a un agente "hormiga" del algoritmo ACO
    """
    def __init__(self):
        pass

    def move(self):
        pass

    def pheromone(self):
        pass

class Colony:
    """
    Implementa el algoritmo ACO básico
    """

    def __init__(self):
        pass

    def optimize(self):
        pass
