import pytest
from classes.grid import Grid
from classes.car import Car
from run_simulation import run_simulation
from functions import DIRECTION

def create_car_A1():
    return Car(
        name="A", x=1, y=2, direction="N", angle=DIRECTION["N"], moves="FFRFFFFRRL"
    )

def create_car_A2():
    return Car(
        name="A", x=0, y=0, direction="E", angle=DIRECTION["S"], moves="FFFRFFFFF"
    )

def create_car_B():
    return Car(
        name="B", x=7, y=8, direction="W", angle=DIRECTION["W"], moves="FFLFFFFFFF"
    )

def create_car_C():
    return Car(
        name="C", x=6, y=1, direction="E", angle=DIRECTION["E"], moves="LFLFRFFF"
    )

def create_car_D():
    return Car(
        name="D", x=5, y=1, direction="E", angle=DIRECTION["E"], moves="FLFLFRFF"
    )


def setup_env(cars) -> Grid:
    """Creates a 10x10 grid and adds the given cars."""
    grid = Grid(10, 10)
    for car in cars:
        grid.add_cars(car)
    return grid


@pytest.mark.parametrize(
    "cars, expected_output",
    [
        pytest.param(
            [create_car_A1()],
            "After simulation, the result is:\n- A, (5,4) S\n",
            id="one_car_in_grid",
        ),
        pytest.param(
            [create_car_A2()],
            "After simulation, the result is:\n- A, (0,0) W\n",
            id="one_car_in_grid_border",
        ),
        pytest.param(
            [create_car_A1(), create_car_B()],
            "After simulation, the result is:\n- A, collides with B at (5,4) at step 7\n- B, collides with A at (5,4) at step 7\n",
            id="two_cars",
        ),
        pytest.param(
            [create_car_A1(), create_car_B(), create_car_C()],
            "After simulation, the result is:\n- A, collides with B,C at (5,4) at step 7\n- B, collides with A,C at (5,4) at step 7\n- C, collides with A,B at (5,4) at step 7\n",
            id="three_cars_1",
        ),
        pytest.param(
            [create_car_A1(), create_car_B(), create_car_D()],
            "After simulation, the result is:\n- A, collides with B at (5,4) at step 7\n- B, collides with A at (5,4) at step 7\n- D, collides with A,B at (5,4) at step 8\n",
            id="three_cars_2",
        ),
    ],
)
def test_simulation(capsys, cars, expected_output):
    """Runs the simulation with different cars and checks the output."""
    run_simulation(setup_env(cars))

    # Capture the output
    captured = capsys.readouterr()

    # Assert expected output
    assert captured.out.strip() == expected_output.strip()
