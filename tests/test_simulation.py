import pytest

from classes.grid import Grid
from classes.car import Car

from run_simulation import run_simulation

from functions import DIRECTION

def test_one_car_simulation(capsys):
    
    carA = Car(name = 'A', x = 1, y = 2, direction = 'N', angle=DIRECTION['N'], moves = 'FFRFFFFRRL')
    
    grid = Grid(10,10)

    grid.add_cars(carA)

    run_simulation(grid)

    # get observed result
    captured = capsys.readouterr()

    #set expected result
    expected_output = "\nAfter simulation, the result is:\n- A, (5,4) S\n"

    assert captured.out == expected_output

def test_two_car_simulation(capsys):
    
    carA = Car(name = 'A', x = 1, y = 2, direction = 'N', angle=DIRECTION['N'], moves = 'FFRFFFFRRL')
    carB = Car(name = 'B', x = 7, y = 8, direction = 'W', angle = DIRECTION['W'], moves = 'FFLFFFFFFF')
    grid = Grid(10,10)

    grid.add_cars(carA)
    grid.add_cars(carB)

    run_simulation(grid)

    # get observed result
    captured = capsys.readouterr()

    #set expected result
    expected_output = "\nAfter simulation, the result is:\n- A, collides with B at (5,4) at step 7\n- B, collides with A at (5,4) at step 7\n"

    assert captured.out == expected_output





    