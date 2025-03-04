import sys

from functions import *

from validations import validate_options_set

POST_SIM_OPTIONS = (
    "\nPlease choose from the following options:\n\n[1] Start over\n[2] Exit\n"
)


def delete_grid(grid):
    """Remove all cars in grid and start simulation"""
    grid.reset_grid()
    start_simulation()


def post_simulation_options(grid):
    """Show post simulation options menu"""
    options_set = {
        "1": {"func": delete_grid, "kwargs": grid},
        "2": {"func": sys.exit, "kwargs": None},
    }
    validate_options_set(prompt=POST_SIM_OPTIONS, options_set=options_set)


def start_simulation():
    """controls the simulation."""

    # 1 initialize grid
    grid = initialize_grid()

    # 2 Ask user to add 1 car, this function will
    #  recursively ask to either add more cars or run simulation
    # until user chooses to run simulation
    add_car(grid)

    # 3 After simulation, ask user to either start over or exit
    post_simulation_options(grid)


if __name__ == "__main__":
    start_simulation()
