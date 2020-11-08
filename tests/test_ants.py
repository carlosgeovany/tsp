import pytest

from tsp.algorithms import Ant
from tsp import Place, Tour


def test_ant_creation(tsp_obj, colony):
    ant = Ant(colony, tsp_obj.places[0])
    t = Tour()
    assert (ant.current == Place(0,0,0) and 
           len(ant.tour) == 0 and
           ant.colony == colony)
    
def test_ants_creation(tsp_obj,colony):
    ants = [Ant(colony, place) for place in tsp_obj.places]
    assert [ant.current.id for ant in ants] == [0,1,2,3,4]