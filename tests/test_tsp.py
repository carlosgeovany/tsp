import pytest

from tsp import Place, Tour


def test_tour_cost(tsp_obj, tour_obj):
    assert [tsp_obj.cost(current, next)
             for current, next in tour_obj] == [1.0, 1.0, 1.0, 2.8284271247461903, 3.605551275463989]
    assert tsp_obj.total_cost(tour_obj) == 9.43397840021018


def test_tsp_creation(tsp_obj):
    assert (Place(0, 0, 0) == tsp_obj.places[0] and 
            Place(1, 1, 0) == tsp_obj.places[1] and 
            Place(2, 0, 1) == tsp_obj.places[2] and 
            Place(3, 1, 1) == tsp_obj.places[3] and 
            Place(4, 2, 3) == tsp_obj.places[4])

def test_missing_places(tsp_obj, tour_obj, t1):
    assert set() == tsp_obj.missing(tour_obj.visited_places)
    assert set([Place(id=3, x=1.0, y=1.0), Place(id=4, x=2.0, y=3.0)]) == tsp_obj.missing(t1.visited_places)