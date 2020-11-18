""" 
Command line interface to solve TSP problem
"""

import warnings

import click

from config import settings
from tsp import TSP
from tsp.solver import Solver

from .utils import process_grid


@click.group()
@click.option(
    "--coordinates_file",
    type=click.File("r"),
    help="Path to the coordinates file",
)
@click.option(
    "--distances_file",
    type=click.File("r"),
    help="Path to the distances/cost file",
)
@click.option(
    "--random",
    is_flag=True,
    help="Generates a random TSP problem. This flag has precedence over the others.",
)
@click.option(
    "--filename", 
    type=click.STRING, 
    help="Full path to the png file solution"
)
@click.pass_context
def main(ctx, coordinates_file, distances_file, random, filename):
    if random:
        tsp = TSP.from_random()
    elif coordinates_file or distances_file:
        tsp = TSP.from_files(coordinates_file, distances_file)
    else:
        warnings.warn("No problem to solve. Is this what you want?")
        return
    ctx.obj["tsp"] = tsp
    ctx.obj["filename"] = filename


@main.command()
@click.pass_context
def solve(ctx):
    grids = settings.algorithms
    algorithms = process_grid(grids)
    solver = Solver(algorithms)
    solution = solver.solve(ctx.obj["tsp"], ctx.obj["filename"])
    print(f"Best solution found with: {solution[0]}\n{solution[1]}")


@main.command()
@click.option(
    "--filename", type=click.STRING, help="Full path to the png file"
)
@click.pass_context
def problem_png(ctx, filename):
    ctx.obj["tsp"].plot_problem(filename)
    print(f"problem plot saved at {filename}")


def start():
    main(obj={})
