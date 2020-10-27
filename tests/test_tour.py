import pytest


from tsp import Tour, Place

@pytest.fixture
def places():
    return {
        'A': Place('A', 0, 0),
        'B': Place('B', 1, 0),
        'C': Place('C', 0, 1),
        'D': Place('D', 1, 1)
    }


def test_tour_closed(places):
    t1 = Tour()
    t1.append(places['A'])
    t1.append(places['B'])

    assert t1.closed == False

    t1.append(places['A'])

    assert t1.closed == True

def test_append_place(places):
    t1 = Tour()
    t1.append(places['A'])

    assert places['A'] == t1.initial

    t1.append(places['B'])

    assert len(t1) == 2

def test_close_tour(places):
    t1 = Tour()
    t1.append(places['A'])


    t1.close()

    assert t1.closed == False

    t1.append(places['B'])

    t1.close()

    assert t1.closed == True

    assert t1.initial  == t1.current
