
import pytest

from tsp import Place
from tsp.algorithms import AntColony, GreedyTSP


def test_greedy(tsp_obj):

    g = GreedyTSP(initial=Place(3, 0, 0))

    solution = g.run(tsp_obj)

    print(solution['tour'])

    assert int(solution['cost']) == 21



def test_aoc(tsp_obj):
    colony = AntColony(alpha=1, beta=1, rho=0.5, Q=100)

    solution = colony.run(tsp_obj)

    assert solution['cost'] == 137
