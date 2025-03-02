from functions import initialize_grid, add_car
from classes.grid import Grid

from validations import validate_options_set

POST_SIM_OPTIONS = (
    "\nPlease choose from the following options:\n\n[1] Start over\n[2] Exit\n"
)

def delete_grid(grid: Grid):
    '''
    This function will remove all cars in grid and start simulation
    '''
    grid.reset_grid()
    start_simulation()

def post_simulation_options(grid):
    # 3 Options menu 2 (Start over or exit)
    options_set = {
        "1": {"func": delete_grid, "kwargs": grid},
        "2": {"func": exit, "kwargs": None},
    }

    choice = input(POST_SIM_OPTIONS)
    validate_options_set(choice=choice, options_set=options_set)

def start_simulation():
    '''
    This function controls the simulation.
    '''
    
    # 1 initialize grid
    grid = initialize_grid()

    # 2 Ask user to add 1 car, this function will
    #  recursively ask to either add more cars or run simulation
    # until user chooses to run simulation
    add_car(grid)

    # After simulation, ask user to either start over or exit
    post_simulation_options(grid)

def main():
    carA = Car('A')
    carB = Car('B')
    grid = Grid(10,10)

    carA.x = 1
    carA.y = 2
    carA.direction = 'N'
    carA.angle = DIRECTION[carA.direction]
    carA.moves = 'FFRFFFFRRL'

    carB.x = 7
    carB.y = 8
    carB.direction = 'W'
    carB.angle = DIRECTION[carB.direction]
    carB.moves = 'FFLFFFFFFF'

    grid.add_cars(carA)
    grid.add_cars(carB)

    run_simulation(grid)

start_simulation()
#main()
