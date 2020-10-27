import pytest
import io
import tsp

from tsp import TSP, Place
from tsp.algorithms import GreedyTSP, AntColony

@pytest.fixture
def tsp_definition():

    tsp = """
    0 20
  -25 0
   30 0
    0 0
    """

    return io.StringIO(tsp)

@pytest.fixture
def tsp_obj(tsp_definition):
    return TSP.from_file(tsp_definition)

def test_greedy(tsp_obj):

    g = GreedyTSP()

    solution = g.run(tsp_obj, current=Place(3,0,0))

    assert int(solution['cost']) == 137

def test_aoc(tsp_obj):
    colony = AntColony(alpha=1, beta=1, rho=0.5, Q=100)

    solution = colony.run(tsp_obj)

    assert solution['cost'] == 137
