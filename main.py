
from prompts import *
    

def main_simulation():

    # 1
    print("Welcome to auto Driving car Simulation.\n\n")

    # 2 Initialize grid
    grid = initialize_grid()

    # Ask user to add cars
    # This function will continue asking user to add cars until user runs simulation
    add_car(grid)

    # Options menu 2 (Start over or exit)
    options_set_2(grid)
      
main_simulation()

# def main():
#     carA = Car('A')
#     carB = Car('B')
#     grid = Grid(10,10)

#     carA.x = 1
#     carA.y = 2
#     carA.direction = 'N'
#     carA.angle = DIRECTION[carA.direction]
#     carA.moves = 'FFRFFFFRRL'

#     carB.x = 7
#     carB.y = 8
#     carB.direction = 'W'
#     carB.angle = DIRECTION[carB.direction]
#     carB.moves = 'FFLFFFFFFF'

#     grid.add_cars(carA)
#     grid.add_cars(carB)

#     run_simulation(grid)

#main()
