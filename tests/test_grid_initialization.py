import pytest
from functions import initialize_grid
from unittest.mock import patch

@pytest.mark.parametrize(
    "inputs, expected_x, expected_y, expected_output",
    [
        pytest.param(
            ["10 10"], 
            10, 10, 
            "Welcome to Auto Driving Car Simulation.\n\n\n\nYou have created a field of 10 x 10\n\n",
            id="valid_grid"
            ),
        pytest.param(
            ["101", "10 10"], 
            10, 10, 
            "Welcome to Auto Driving Car Simulation.\n\n\nInvalid input. Please try again\n\n\nYou have created a field of 10 x 10\n\n",
            id="invalid_grid"
        ),
    ]
)
def test_grid_initialization(capsys, inputs, expected_x, expected_y, expected_output):
    """Test grid initialization with valid and invalid inputs."""
    with patch("builtins.input", side_effect=inputs):
        grid = initialize_grid()
        captured = capsys.readouterr()
        
        assert grid.max_x == expected_x
        assert grid.max_y == expected_y
        assert captured.out == expected_output