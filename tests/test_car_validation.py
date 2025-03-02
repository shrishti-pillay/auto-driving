from classes.car import Car
from classes.grid import Grid
from functions import get_x_y_direction, get_moves

from unittest.mock import patch

def test_car_x_y_direction_1():
    with patch("builtins.input", side_effect=["1 2 N"]):
        #setup test environment
        x, y, direction = get_x_y_direction(Car('A'), Grid(10,10))
        
        assert x == '1'
        assert y == '2'
        assert direction == 'N'

def test_car_x_y_direction_2(capsys):
    with patch("builtins.input", side_effect=["1 24 N", "1 2 N"]):
        #setup test environment
        x, y, direction = get_x_y_direction(Car('A'), Grid(10,10))
        
        captured = capsys.readouterr()

        assert x == '1'
        assert y == '2'
        assert direction == 'N'
        assert captured.out == "Invalid input. Please try again\n\n"

def test_car_moves_1():
    with patch("builtins.input", side_effect=["FFRFFFFRRL"]):
        #setup test environment
        moves = get_moves(Car('A'))
        
        assert moves == "FFRFFFFRRL"

def test_car_moves_2(capsys):
    with patch("builtins.input", side_effect=["FFRFFWFRRL", "FFRFFFFRRL"]):
        #setup test environment
        moves = get_moves(Car('A'))
        
        captured = capsys.readouterr()

        assert moves == "FFRFFFFRRL"
        assert captured.out == "Invalid input. Please try again\n\n"