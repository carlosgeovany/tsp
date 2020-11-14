import pytest


from tsp.utils import process_grid, load_algorithm, flatten_algorithm_grid
   

def test_process_grid(grids):
    assert len(process_grid(grids)) == 25


def test_load_algorithm(grids):
    grid = grids[1]
    classpath = grid['algorithm']
    algorithms = []
    hp_grid = grid['hyperparameters']
    for hyperparameters in flatten_algorithm_grid(hp_grid):
        algorithms.append(load_algorithm(classpath, **hyperparameters))
    assert (algorithms[0].alpha == 0.5 and
            algorithms[10].beta == 5.0 and
            algorithms[20].rho == 0.5 and
            algorithms[-1].Q == 100)


def test_flatten_algorithm_grid(grids):
    hp_grids = []
    for grid in grids:
        if 'hyperparameters' in grid:
            hp_grid = grid['hyperparameters']
            for hyperparameters in flatten_algorithm_grid(hp_grid):
                hp_grids.append(hyperparameters)
    assert (hp_grids[0] == {'Q': 10, 'alpha': 0.5, 'beta': 1.0, 'rho': 0.5} and
            hp_grids[10] == {'Q': 10, 'alpha': 1.0, 'beta': 5.0, 'rho': 0.5} and
            hp_grids[20] == {'Q': 100, 'alpha': 1.0, 'beta': 2.0, 'rho': 0.5} and
            hp_grids[-1] == {'Q': 100, 'alpha': 1.0, 'beta': 5.0, 'rho': 0.8})

