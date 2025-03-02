import pytest

from functions import initialize_grid

from unittest.mock import patch

def test_grid_initialization_1():

    with patch("builtins.input", side_effect=["10 10"]):
        # setup test environment
        grid = initialize_grid()

        # compare actual with expected
        assert grid.max_x == 10
        assert grid.max_y == 10

def test_grid_initialization_2(capsys):

    with patch("builtins.input", side_effect=["101", "10 10"]):
        # setup test environment
        grid = initialize_grid()

        # get actual result
        captured = capsys.readouterr()
        # compare actual with expected
        assert grid.max_x == 10
        assert grid.max_y == 10
        assert captured.out  == "Welcome to Auto Driving Car Simulation.\n\n\nInvalid input. Please try again\n\n\nYou have created a field of 10 x 10\n\n"

        


