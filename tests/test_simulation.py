from classes.grid import Grid
from classes.car import Car

from run_simulation import run_simulation

from functions import DIRECTION

def create_car_A():
    return Car(name = 'A', x = 1, y = 2, direction = 'N', angle=DIRECTION['N'], moves = 'FFRFFFFRRL')

def create_car_B():
    return Car(name = 'B', x = 7, y = 8, direction = 'W', angle = DIRECTION['W'], moves = 'FFLFFFFFFF')

def create_car_C():
    return Car(name = 'C', x = 5, y = 1, direction = 'E', angle = DIRECTION['E'], moves = 'FLFLFRFFF')

def setup_env(cars):

    grid = Grid(10,10)
    for car in cars: grid.add_cars(car)

    return grid

def test_one_car_simulation(capsys):
    '''
    Test simulation results with one car
    '''
    
    # setup test environment
    carA = create_car_A()
    run_simulation(setup_env([carA]))

    # get observed result
    captured = capsys.readouterr()

    #set expected result
    expected_output = "\nAfter simulation, the result is:\n- A, (5,4) S\n"

    assert captured.out == expected_output

def test_two_car_simulation(capsys):
    '''
    Test simulation results with two cars
    '''
    
    # setup test environment
    carA = create_car_A()
    carB = create_car_B()
    run_simulation(setup_env([carA, carB]))

    # get observed result
    captured = capsys.readouterr()

    #set expected result
    expected_output = "\nAfter simulation, the result is:\n- A, collides with B at (5,4) at step 7\n- B, collides with A at (5,4) at step 7\n"

    assert captured.out == expected_output

def test_three_car_simulation(capsys):
    '''
    Test simulation results with three cars
    '''
    
    # setup test environment
    carA = create_car_A()
    carB = create_car_B()
    carC = create_car_C()
    run_simulation(setup_env([carA, carB, carC]))

    # get observed result
    captured = capsys.readouterr()

    #set expected result
    expected_output = "\nAfter simulation, the result is:\n- A, collides with B,C at (5,4) at step 7\n- B, collides with A,C at (5,4) at step 7\n- C, collides with A,B at (5,4) at step 8\n"

    assert captured.out == expected_output





    