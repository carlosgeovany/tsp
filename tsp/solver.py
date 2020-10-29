from tsp import TSP

class Solver:
    def __init__(self, algorithms):
        self.algorithms = algorithms


    def solve(self, tsp):
        for algorithm in self.algorithms:
            algorithm.run(tsp)
