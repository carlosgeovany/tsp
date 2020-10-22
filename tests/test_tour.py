import pytest

from tsp import Tour, Place

def test_tour_closed():
    t1 = Tour()
    t1.append(Place(0,0))
    t1.append(Place(1,0))

    assert t1.is_closed() == False
    
    t1.append(Place(0,0))

    assert t1.is_closed() == True
    
def test_append_place():
    t1 = Tour()
    t1.append(Place(0,0))

    assert Place(0,0) == t1.path[0]

    t1.append(Place(1,0))
    
    assert len(t1.path) == 2
    
def test_close_tour():
    t1 = Tour()
    t1.append(Place(0,0))


    t1.close()

    assert t1.is_closed() == False

    t1.append(Place(1,0)) 

    t1.close()

    assert t1.is_closed() == True

    assert t1.path[0]  == t1.path[-1]
