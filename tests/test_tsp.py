import pytest
import io
import tsp

@pytest.fixture
def tsp_definition():

    tsp = """
    0 0
    1 0
    0 1
    1 1
    """

    return io.StringIO(tsp)

@pytest.fixture
def tsp_obj(tsp_definition):
    return tsp.TSP.from_file(tsp_definition)


@pytest.fixture
def tour_obj():
    t = tsp.Tour()

    t.append(tsp.Place(0,0,0))
    t.append(tsp.Place(1,1,0))
    t.append(tsp.Place(3,1,1))
    t.append(tsp.Place(2,0,1))
    t.close()

    return t


def test_tour_cost(tsp_obj, tour_obj):
    for current,next in tour_obj:
        assert tsp_obj.cost(current, next) == 1

    assert tsp_obj.total_cost(tour_obj) == 4

def test_tsp_creation(tsp_obj):
    assert tsp.Place(0,0,0) == tsp_obj.places[0] and \
        tsp.Place(1,1,0) == tsp_obj.places[1] and \
        tsp.Place(2,0,1) == tsp_obj.places[2] and \
        tsp.Place(3,1,1) == tsp_obj.places[3]

def test_missing_places(tsp_obj):
    tour = tsp.Tour()
    tour.append(tsp_obj.places[0])
    tour.append(tsp_obj.places[1])

    assert set([tsp_obj.places[2], tsp_obj.places[3]]) == tour.missing(tsp_obj.places)
