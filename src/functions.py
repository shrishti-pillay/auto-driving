from classes.car import Car
from classes.grid import Grid

from run_simulation import *
from validations import *


INITIALIZE_GRID = (
    "Please enter the width and height of the simulation field in x y format:\n"
)

CAR_NAME = "Please enter the name of the car:\n"

CAR_X_Y_DIRECTION = "Please enter initial position of car {} in x y Direction format:\n"

CAR_COMMANDS = "Please enter the commands for car {}:\n"

OPTIONS_MENU = "Please choose from the following options:\n\n[1] Add a car to the field\n[2] Run simulation\n"


def initialize_grid() -> Grid:
    """Initialize the grid by prompting the user for width and height."""

    # Welcome statement
    print("Welcome to Auto Driving Car Simulation.\n\n")

    # get x y for grid
    max_x, max_y = get_valid_input(
        prompt=INITIALIZE_GRID, validation_func=validate_grid_dimensions, split_count=2
    )

    # Create grid, subtract 1 from limits 
    grid = Grid(int(max_x)-1, int(max_y)-1)

    print(f"\nYou have created a field of {max_x} x {max_y}\n")
    return grid

def get_car_name(grid: Grid):
    """ Get car name."""

    name = get_valid_input(
        prompt=CAR_NAME,
        validation_func=validate_car_name,
        split_count=1,
        names = [x.name for x in grid.cars if grid.cars]
    )

    return name[0]

def get_x_y_direction(name: str, grid: Grid) -> list:
    """Get x, y, and direction for the car."""

    return get_valid_input(
        prompt=CAR_X_Y_DIRECTION.format(name),
        validation_func=validate_car_x_y_direction,
        split_count=3,
        max_x=grid.max_x,
        max_y=grid.max_y,
    )


def get_moves(name: str) -> str:
    """Get car commands"""

    moves = get_valid_input(
        prompt=CAR_COMMANDS.format(name),
        validation_func=validate_car_commands,
        split_count=1,
    )
    return moves[0]


def add_car(grid: Grid) -> None:
    """
    This function adds the first car to the grid, and any
    subsequent cars if user chooses to.
    """

    # get car name
    name = get_car_name(grid)

    # get x y direction of car
    x, y, direction = get_x_y_direction(name, grid)

    # get car angle form direction
    angle = DIRECTION[direction]

    # get car commands (moves)
    moves = get_moves(name)

    # create car
    car = Car(name, int(x), int(y), direction, angle, moves)

    # add car to grid
    grid.add_cars(car)

    # show all the cars in the grid
    print(f"Your current list of cars are:\n")
    for car in grid.cars:
        print(f"- {car.name}, ({car.x},{car.y}), {car.direction}, {car.moves}\n")

    # show options menu (add more cars or run simulation)
    options_set(grid)


def options_set(grid: Grid) -> None:
    """
    This function asks the user to choose to
    either add more cars, or run simulation
    """
    options_set = {
        "1": {"func": add_car, "kwargs": grid},
        "2": {"func": run_simulation, "kwargs": grid},
    }
    validate_options_set(prompt=OPTIONS_MENU, options_set=options_set)
