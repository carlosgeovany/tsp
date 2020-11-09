"""
"""

class Solver:
    """"""

    def __init__(self, algorithms):
        self.algorithms = algorithms
        self.solutions = {}

    def solve(self, tsp):
        print(f"Will use {len(self.algorithms)} algorithms to solve this problem.")
        for algorithm in self.algorithms:
            print(f"Solving TSP problem with {algorithm}")
            self.solutions[str(algorithm)] = algorithm.run(tsp)
        
        return self.solutions
        