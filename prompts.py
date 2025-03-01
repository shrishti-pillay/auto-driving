from classes.car import Car
from classes.grid import Grid

from validators import validate_choice
from simulation import *


def initialize_grid() -> Grid:
    max_x = ''
    max_y = ''

    while not (max_x or max_y):
        grid_coord = input(
        "Please enter the width and height of the simulation fields in x y format.\n"
        )
        try:
            max_x, max_y = grid_coord.split(" ")
        except:
            print("You have entered an invalid grid dimension.\nPlease try again\n")
            continue

        try:
            # 3 Set grid dimensions
            grid = Grid(max_x, max_y)
        except:
            print("You have entered invalid values for the x y grid dimensions.\nPlease try again\n")
            max_x = ''
            max_y = ''
            continue

        print(f"\nYou have created a field of {max_x} x {max_y}\n")
    
    return grid

def add_car(grid):
    
    name = input("Plese enter the name of the car:\n")

    # add car to grid
    car = Car(name)
    grid.add_cars(car)

    position = input(
        f"Please enter initial position of car {name} in x y Direction format.\n\n"
    )

    try:
        x, y, direction = position.split(" ")
    except:
        print("You have entered an invalid input. \nPlease try again.")

    # if x > grid.max_x or x < MIN_X or y > grid.max_y or y < MIN_Y:

    car.x = x
    car.y = y

    """ add direction validation"""

    car.direction = direction

    ''' get angle from direction '''

    car.angle = DIRECTION[car.direction]

    commands = input(f"Please enter the commands for car {name}\n")

    car.moves = commands

    print(f"Your current list of cars are:\n")

    for car in grid.cars:
        print(f" - {car.name}, ({car.x},{car.y}), {car.direction}, {car.moves}\n")

    options_set_1(grid)

def options_set_1(grid):
    choice = input(
        "Please choose from the following options:\n\n[1] Add a car to the field\n[2] Run simulation\n\n"
    )
    if choice == "1":
        add_car(grid)
    elif choice == "2":
        run_simulation(grid)
    else: 
        print("Invalid choice. Please try again.")
        options_set_1(grid)

def options_set_2(grid):
    choice = input(
        "\nPlease choose from the following options:\n\n[1] Start over\n[2] Exit\n"
    )
    if choice == '1':
        for car in grid.cars:
            del car
        del grid
        initialize_grid()
    elif choice == '2': 
        exit()
    else: 
        print("Invalid choice. Please try again.")
        options_set_2(grid)