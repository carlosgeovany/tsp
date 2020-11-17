"""
Run tsp problem with TSPGreedy and AOC algorithms
Returns best solution for TSP problem and plot solution
"""
from copy import copy
import matplotlib.pyplot as plt


class Solver:
    """"""

    def __init__(self, algorithms):
        self.algorithms = algorithms
        self.solutions = {}

    
    def plot_solution(self, tsp, best, filename):
        """
        PLot and save the best solution
        """
        best_tour = copy(best[1]["tour"])

        for place in tsp.places:
            plt.plot(place.x, place.y, "bo")

        for current, next in best_tour:
            plt.arrow(
                current.x,
                current.y,
                next.x - current.x,
                next.y - current.y,
                color="b",
                length_includes_head=True,
                head_width = 1.5
            )

        plt.annotate(
            "initial",
            xy=(best_tour.initial.x, best_tour.initial.y),
            xytext=(best_tour.initial.x, best_tour.initial.y)
        )

        plt.title("TSP solution cost: %.2f" % best[1]["cost"])
        plt.savefig(filename)    


    def solve(self, tsp, filename):
        """
        Run Greedy and AOC algorithms to find the best solution
        """
        print(
            f"Will use {len(self.algorithms)} algorithms to solve this problem."
        )
        for algorithm in self.algorithms:
            print(f"Solving TSP problem with {algorithm}")
            self.solutions[str(algorithm)] = algorithm.run(tsp)

        best = min(self.solutions.items(), key=lambda x: x[1]["cost"])
        self.plot_solution(tsp, best, filename)

        return best
