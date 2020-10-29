""" Una interfaz de línea de comandos para resolver el TSP con diversos algoritmos"""
import click

from dynaconf import settings

from tsp.solver import Solver

@click.command()
@click.option('--random', is_flag=True)
@click.option('--tsp-file', type=click.File('r'))
def solve(random, tsp_file):
    print(f"Hola desde cli: {random}")
