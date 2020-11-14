"""
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import distance
from dataclasses import dataclass
from typing import List
from more_itertools import pairwise



class TSP:
    """
    Describe a TSP
    """
    def __init__(self, coordinates,*distances):
        self.places = [Place(id, v[0], v[1]) for id, v in enumerate(coordinates)]
        self.distances = distance.cdist(coordinates, coordinates, 'euclidean')

    def cost(self, place, another_place):
        return self.distances[place.id][another_place.id]

    def total_cost(self, tour):
        total_cost = 0.0
        for current, next in tour:
            total_cost += self.cost(current, next)
        return total_cost

    def missing(self, visited_places):
        return set(self.places).difference(visited_places)

    @classmethod
    def from_files(self,coordinates_file, distances_file):
        coordinates = np.loadtxt(coordinates_file)
        distances = np.loadtxt(distances_file)
        return self(coordinates, distances)

    @classmethod
    def from_random(self, num_places=50, max_distance=100):
        coordinates = np.random.randint(low=0, high=max_distance, size=(num_places,2))
        return self(coordinates)
    
    def plot_problem(self, filename):
        for place in self.places:
            plt.plot(place.x, place.y, 'bo')
        plt.title("Places to visit in TSP")
        plt.savefig(filename)
    
    
    



@dataclass(eq=True,frozen=True)
class Place:
    """
    A place to be visited
    """
    id: int
    x: float
    y: float

class Tour:
    """
    Describes places visited
    """
    def __init__(self):
        self._path = []

    @property
    def initial(self):
        return self._path[0]

    @property
    def current(self):
        return self._path[-1]

    @property
    def closed(self):
        closed = False
        if len(self._path) > 1:
            closed = self._path[0] == self._path[-1]

        return closed

    @property
    def visited_places(self):
        return set (self._path)

    def close(self):
        if len(self._path) > 1:
            self._path.append(self._path[0])

    def append(self, place):
        self._path.append(place)

    def __len__(self):
        return len(self._path)


    def __iter__(self):
        return ((current, next) for (current,next) in pairwise(self._path))


    def __repr__(self):
        return f"Tour: [{'->'.join([str(place) for place in self._path])}]"


    def __str__(self):
        return f"Tour: [{'->'.join([place.id for place in self._path])}]"

    
__version__ = '0.1.1'


#from .cli import cli
