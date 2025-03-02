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
    '''
    This function will get the x y field of the grid and initialize the grid object

    Args: None
    Returns: None

    '''
    # 1
    print("Welcome to Auto Driving Car Simulation.\n\n")

    # get x y for grid
    max_x, max_y = get_valid_input(
        prompt=INITIALIZE_GRID, validation_func=validate_grid_dimensions, split_count=2
    )

    # Create grid
    grid = Grid(int(max_x), int(max_y))

    print(f"\nYou have created a field of {max_x} x {max_y}\n")
    return grid


def add_car(grid: Grid) -> None:
    '''
    This function adds the first car to the grid, and any subsequent cars if user chooses to.
    
    Args: 
        grid: The current grid
    Returns: None
    
    '''

    # get car name
    name = input(CAR_NAME)
    car = Car(name)

    # add car to grid
    grid.add_cars(car)

    # get x y direction of car
    x, y, direction = get_valid_input(
        prompt=CAR_X_Y_DIRECTION.format(car.name),
        validation_func=validate_car_x_y_direction,
        split_count=3,
        max_x=grid.max_x,
        max_y=grid.max_y,
    )

    # set x y direction of car
    car.x = x
    car.y = y
    car.direction = direction

    # get car angle form direction
    car.angle = DIRECTION[car.direction]

    car.moves = get_valid_input(
        prompt=CAR_COMMANDS.format(car.name),
        validation_func=validate_car_commands,
        split_count=1,
    )[0]

    print(f"Your current list of cars are:\n")

    for car in grid.cars:
        print(f" - {car.name}, ({car.x},{car.y}), {car.direction}, {car.moves}\n")

    options_set(grid)


def options_set(grid: Grid) -> None:
    '''
    This function asks the user to choose to either add more cars, or run simulation
    
    Args: 
        grid: The current Grid
        
    Returns: None
    
    '''
    options_set = {
        "1": {"func": add_car, "kwargs": grid},
        "2": {"func": run_simulation, "kwargs": grid},
    }
    choice = input(OPTIONS_MENU)
    validate_options_set(choice=choice, options_set=options_set)
