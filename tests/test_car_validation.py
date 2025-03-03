import pytest
from classes.car import Car
from classes.grid import Grid
from functions import get_x_y_direction, get_moves
from unittest.mock import patch

@pytest.mark.parametrize(
    "inputs, expected_x, expected_y, expected_direction, expected_output",
    [
        pytest.param(
            ["1 2 N"], "1", "2", "N", "", 
            id="valid_x_y_direction"
        ),
        pytest.param(
            ["1 24 N", "1 2 N"], "1", "2", "N", 
            "Invalid input. Please try again\n\n",
            id="invalid_y"
        ),
        pytest.param(
            ["1 2 U", "1 2 N"], "1", "2", "N", 
            "Invalid input. Please try again\n\n",
            id="invalid_direction"
        ),
    ]
)
def test_car_x_y_direction(capsys, inputs, expected_x, expected_y, expected_direction, expected_output):
    """Test car x, y direction with valid and invalid inputs."""
    with patch("builtins.input", side_effect=inputs):
        x, y, direction = get_x_y_direction(Car('A'), Grid(10, 10))
        captured = capsys.readouterr()
        
        assert x == expected_x
        assert y == expected_y
        assert direction == expected_direction
        assert captured.out == expected_output

@pytest.mark.parametrize(
    "inputs, expected_moves, expected_output",
    [
        pytest.param(
            ["FFRFFFFRRL"], 
            "FFRFFFFRRL", "",
            id="valid_moves"
        ),
        pytest.param(
            ["FFRFFWFRRL", "FFRFFFFRRL"], 
            "FFRFFFFRRL", 
            "Invalid input. Please try again\n\n",
            id="invalid_moves"
        ),
    ],
)
def test_car_moves(capsys, inputs, expected_moves, expected_output):
    """Test car move commands with valid and invalid inputs."""
    with patch("builtins.input", side_effect=inputs):
        moves = get_moves(Car('A'))
        captured = capsys.readouterr()
        
        assert moves == expected_moves
        assert captured.out == expected_output
