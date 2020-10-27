import numpy as np
import copy

from abc import ABC, abstractmethod

from tsp import Tour


class Algorithm(ABC):

    @abstractmethod
    def run(self, problem, *args):
        pass

class GreedyTSP(Algorithm):
    def __init__(self):
        pass

    def run(self, tsp, current):
        """
        Selecciona los siguientes nodos a visitar de manera greedy
        """

        if current is None:
            current = np.random.choice(tsp.places)


        tour = Tour()
        tour.append(current)

        while not tour.closed:

            distances_to = {next_place: tsp.cost(current, next_place) for next_place in tour.missing(tsp.places)}

            current = min(distances_to, key=distances_to.get)
            tour.append(current)

            if len(tour) == len(tsp.places):
                tour.close()

        cost = tsp.total_cost(tour)

        return {'cost': cost, 'tour': tour}

class Ant:
    """
    Representa a un agente "hormiga" del algoritmo ACO
    """
    def __init__(self, colony, initial_state):
        self.current = initial_state
        self.tour = Tour()
        self.colony = colony

    def smell(self, other):
        return self.colony.pheromones[self.current][other]**self.colony.alpha * self.colony.eta[self.current][other]**self.colony.beta

    @property
    def not_visited(self):
        return set(self.colony.places).difference(set(self.tour))

    @property
    def tour_finished(self):
        return False if self.not_visited else True

    def move(self):
        odor = 0.0

        for next in self.not_visited:
            odor += self.smell(next)

        threshold = np.random.rand()
        for next in not_visited:
            prob_current_next = self.smell(next)/odor
            threshold -= prob_current_next
            if threshold <= 0:
                self.current = next
                self.tour.append(next)

    def travel(self):
        while not tour_finished:
            self.move()

class AntColony:
    """
    Implementa el algoritmo ACO básico
    """

    def __init__(self, alpha, beta, rho, Q, max_steps=100):
        self.alpha = alpha
        self.beta = beta
        self.rho = rho
        self.Q = Q
        self.best = None
        self.steps = 0
        self.max_steps = max_steps

    def init(self):
        self.ants = [Ant(self, place) for place in self.tsp.places ]
        self.initial_pheromone = 1.0/len(self.tsp.places)
        self.pheromones = np.full([len(self.tsp.places), len(self.tsp.places)], fill_value=self.initial_pheromone)
        self.eta = (1/self.tsp.distances)

    def reset(self):
        self.init()


    @property
    def places(self):
        return self.tsp.places

    @property
    def done(self):
        return self.steps > self.max_steps

    def update_pheromones(self):
        self.pheromones *= (1.0 - self.rho)
        self.pheromones[self.pheromones < 0.0] = self.initial_pheromone

        for ant in self.ants:
            for (current, next) in ant.tour:
                self.pheromones[current][to] += Q/len(ant.tour)
                self.pheromones[next][current] = self.pheromones[current][to]

        self.pheromones *= self.rho

    def update_best(self):
        for ant in self.ants:
            if len(ant.tour) < len(self.best):
                self.best = copy(ant.tour)

    def step(self):
        for ant in self.ants:
            ant.move()

        self.update_best()
        self.update_pheromones()
        self.steps += 1

    def run(self, tsp):
        self.tsp = tsp
        self.init()
        while not self.done:
            self.step()
