import io

import pytest

import tsp

def test_tour_cost(tsp_obj, tour_obj):
    assert [tsp_obj.cost(current, next)
            for current, next in tour_obj] == [3, 6, 5, 8, 7]
    assert tsp_obj.total_cost(tour_obj) == 29


def test_tsp_creation(tsp_obj):
    assert tsp.Place(0, 0, 0) == tsp_obj.places[0] and \
        tsp.Place(1, 1, 0) == tsp_obj.places[1] and \
        tsp.Place(2, 0, 1) == tsp_obj.places[2] and \
        tsp.Place(3, 1, 1) == tsp_obj.places[3]


def test_missing_places(tsp_obj):
    tour = tsp.Tour()
    tour.append(tsp_obj.places[0])
    tour.append(tsp_obj.places[1])

    assert set([tsp_obj.places[2], tsp_obj.places[3], tsp_obj.places[4]]
               ) == tour.missing(tsp_obj.places)
