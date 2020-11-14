"""
Run tsp problem with TSPGreedy and AOC algorithms
Returns best solution for TSP problem and plot solution
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
        
        best = min(self.solutions.items(), key=lambda x: x[1]['cost'])
        
        def plot_solution(best):
            for place in best.places:
                    plt.plot(place.x, place.y, 'bo')

            for current, next in best.tour:
                plt.arrow(current.x, current.y,
                          next.y - current.x, next.y - current.y,
                          color='b', length_includes_head=True)


            # Close the loop
            last = self.tour[-1]
            first = self.tour[0]
            plt.arrow(self.place[last].x, self.place[last].y,
                          self.place[first].x - self.place[last].x, self.place[first].y - self.place[last].y,
                          color='b', length_includes_head=True)

            plt.show()
        
        #plot_solution(best)
        
        print(best[1])
        
        return best
        