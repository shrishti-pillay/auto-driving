import pytest

from classes.grid import Grid
from functions import options_set
from main import post_simulation_options

from unittest.mock import patch

@pytest.mark.parametrize(
    "input, expected_output",
    [
        pytest.param(
            ["1","A","1 2 N","FFRFFFFRRL","2"],
            "Your current list of cars are:\n\n- A, (1,2), N, FFRFFFFRRL\n\nAfter simulation, the result is:\n- A, (5,4) S\n",
            id="options_set_valid",
        ),
        pytest.param(
            ["3","1","A","1 2 N","FFRFFFFRRL","2"],
            "Invalid choice. Please try again\n\nYour current list of cars are:\n\n- A, (1,2), N, FFRFFFFRRL\n\nAfter simulation, the result is:\n- A, (5,4) S\n",
            id="options_set_invalid",
        ),
    ],
)
def test_options_set(capsys, input, expected_output):
    ''' Test valid choice 1 and 2 from options set 
    
    [1] Add car to the gird
    [2] Run simulation
    '''

    with patch("builtins.input", side_effect=input):
        #setup test environment
        options_set(Grid(10,10))

        # Capture the output
        captured = capsys.readouterr()

        # Assert expected output
        assert captured.out.strip() == expected_output.strip()

@pytest.mark.parametrize(
    "input, expected_output",
    [
        pytest.param(
            ["1", "10 10", "A","1 2 N","FFRFFFFRRL","2","2"],
            "Welcome to Auto Driving Car Simulation.\n\nYou have created a field of 10 x 10\nYour current list of cars are:\n\n- A, (1,2), N, FFRFFFFRRL\n\nAfter simulation, the result is:\n- A, (5,4) S\n",
            id="post_sim_options_valid",
        ),
        pytest.param(
            ["3", "2"],
            "Invalid choice. Please try again\n",
            id="post_sim_options_invalid",
        ),
    ],
)

def test_post_sim_options_set(capsys, input, expected_output):
    ''' Test valid choice 1 and 2 from options set 
    
    [1] Start over
    [2] Exit
    '''
    with patch("builtins.input", side_effect=input):
        with pytest.raises(SystemExit) as exc_info:
            #setup test environment
            post_simulation_options(Grid(10,10))

            captured = capsys.readouterr()
        
            assert captured.out == expected_output
            assert exc_info.type == SystemExit