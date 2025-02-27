from grid import Grid
from car import Car
from helper import *

MIN_X = 0
MAX_X = 0



def main_simulation():


    
    #1
    print("Welcome to auto Driving car Simulation.\n\n")

    #2 
    grid_coord = input("Please enter the width and height of the simulation fiels in x y format.\n\n")

    ''' add grid validation'''

    max_x, max_y = grid_coord.split(' ')

    #3 Set grid dimensions
    grid = Grid(max_x, max_y)
    
    choice = ''
    

    if len(grid.cars) > 0:
        choice = input("Please choose from the following options:\n\n[1] Add a car to the field\n[2] Run simulation\n\n")

    ''' add choice validation '''

    if choice == '1' or len(grid.cars) == 0: 

        name = input("Plese enter the name of the car:\n")

        # add car to grid
        car = Car(name)
        grid.add_cars(car)

        position = input(f"Please enter initial position of car {name} in x y Direction format.\n\n")

        ''' add car pos validation '''

        x, y, direction = position.split(' ')

        car.x = x
        car.y = y

        ''' add direction validation'''
        
        car.direction = direction

        print(car)

        




main_simulation()


    

