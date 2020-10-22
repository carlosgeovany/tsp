"""
"""

import numpy as np
from scipy.spatial import distance
from dataclasses import dataclass
from typing import List


class TSP:
    """
    Describes a TSP
    """
    def __init__(self, coordinates):
        self.places = [Place(v[0], v[1]) for v in coordinates]

        self.distances = distance.cdist(coordinates, coordinates, 'euclidean')

        self.initial_pheromone =  1.0 / len(self.places)

        self.pheromones = np.full([len(self.places), len(self.places)], fill_value=self.initial_pheromone)



    def total_cost(self, tour):
        pass

    @staticmethod
    def from_file(filepath):
        coordinates = np.fromfile(filepath, sep=" ")
        return TSP(coordinates)

    @staticmethod
    def from_random(num_places=50, max_distance=100):
        coordinates = np.random.randint(low=0, high=max_distance, size=(num_places,2))
        return TSP(coordinates)

@dataclass
class Place:
    """A place to be visited"""
    x: float
    y: float

class Tour:
    """"""
    def __init__(self):
        self.path = []

    def __str__(self):
        return '->'.join(self.path)

    def append(self, place):
        pass

    
class Solver:

    def __init__(self, algorithms):
        self.algorithms = algorithms


    def solve(self, tsp):
        for algorithm in self.algorithms:
            algorithm.run(tsp)

__version__ = '0.1.0'


#from .cli import cli
