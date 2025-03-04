# Auto Driving Car Simulation

## 1. Description
The purpose of this project is to run an auto driving car simulation. 

The simulation program is designed to work with a rectangular field, specified by its width and height. The bottom left coordinate of the field is at position (0,0), and the top right position is denoted (width,height). For example, a field with dimensions 10 x 10 would have its upper right coordinate at position (9,9).

One or more cars can be added to the field, each with a unique name, starting position, and direction they are facing. For instance, a car named "A" may be placed at position (1,2) and facing North.

A list of commands can be issued to each car, which can be one of three commands:

- L: rotates the car by 90 degrees to the left
- R: rotates the car by 90 degrees to the right
- F: moves forward by 1 grid point

If a car tries to move beyond the boundary of the field, the command is ignored, and the car stays in its current position. For example, if a car at position (0,0) is facing South and receives an F command, the command will be ignored as it would take the car beyond the boundary of the field.

Users can interact with the simulation program through the command line interface.

## 2. Installation

### 2.1 Pre-requisites

- Python version **3.8** and above.
- `pip` (Python package installer)

### 2.2 Setup 

1. Clone the git repository

```shell
git clone https://github.com/yourusername/auto-driving.git
```

2. Create a new virtual environment in the main project directory `auto-driving/`. 

```shell
python3 -m venv .env
```

3. Activate the environment with the command:

```shell
source .env/bin/activate
```

You are now running the virtual environment. 

4. Install the auto driving car simulation package using the following command at the main directory. 

```shell
python3 -m pip install -e .
```

## 3. Execution

You can now run the simulation by using the following command: 

```shell
python3 src/main.py
```

### 3.1. Initialise the Grid

You will be first asked to enter the grid dimensions:

```
Please enter the width and height of the simulation field in x y format:

> 10 10
```

### 3.2 Add cars

You will be then asked to name your first car. 

```
Please enter the name of the car:
> A
```

You will then be asked to add initial position and direction of the car. 

```
Please enter initial position of car A in x y Direction format:
> 1 2 N
```

You will then be asked to enter car commands: 

```
Please enter the commands for car A:
> FFRFFFFRRL
```

You will then view the list of cars in the grid. 

```
Your current list of cars are:
- A, (1,2) N, FFRFFFFRRL
```

You can then choose to either continue adding more cars or run the simulation, 

### 3.3 Add more cars or run simulation

```
Please choose from the following options:
[1] Add a car to field
[2] Run simulation
```
If you choose 1, the above steps will be repeated.  
If you choose 2, the simulation will run and display the results.


### 3.4 Simulation results
```
After simulation, the result is:
- A, (5,4) S
```

And then you can either start over or exit the simulation. 

```
Please choose from the following options:
[1] Start over
[2] Exit
```

If you choose 1, the simulation will start over from step 3.1. where you initialise the grid. All the past data will be gone. 

If you choose 2, you exit the simulation. 


## 4. Testing

To run all the tests included, please run the following command in the main project directory:

```
pytest -vv
```

You can increase or reduce the verbosity of the testing set by removing/adding to the -v argument.

To run a test simulation, please run the following command in the main project directory:

```
pytest tests/test_simulation.py
```

The above test includes the following test scenarios: 

#### 1. one_car_in_grid
Objective: Test simulation with one car.

Input: 

    Your current list of cars are:
    - A, (1,2) N, FFRFFFFRRL

Output: 

    After simulation, the result is:
    - A, (5,4) S

#### 2.one_car_in_grid_border
Objective: Test simulation with one car at 0,0 border of the grid.

Input: 

    Your current list of cars are:
    - A, (0,0) S, FFFRFFFFF

Output: 

    After simulation, the result is:
    - A, (0,0) W

#### 3. two_cars
Objective: Test simulation with two cars. 
Input: 

    Your current list of cars are:
    - A, (1,2) N, FFRFFFFRRL
    - B, (7,8) W, FFLFFFFFFF

Output: 

    After simulation, the result is:
    - A, collides with B at (5,4) at step 7
    - B, collides with A at (5,4) at step 7

#### 4. three_cars_1
Objective: Test simulation with three cars where all cars collide with each other at the same time. 

Input: 

    Your current list of cars are:
    - A, (1,2) N, FFRFFFFRRL
    - B, (7,8) W, FFLFFFFFFF
    - C, (6,1) E, LFLFRFFF

Output: 

    After simulation, the result is:
    - A, collides with B,C at (5,4) at step 7
    - B, collides with A,C at (5,4) at step 7
    - C, collides with A,B at (5,4) at step 7

#### 4. three_cars_2
Objective: Test simulation with three cars where the third car collides with two other cars that collided previously. 

Input: 

    Your current list of cars are:
    - A, (1,2) N, FFRFFFFRRL
    - B, (7,8) W, FFLFFFFFFF
    - D, (5,1) E, FLFLFRFF

Output: 

    After simulation, the result is:
    - A, collides with B at (5,4) at step 7
    - B, collides with A at (5,4) at step 7
    - D, collides with A,B at (5,4) at step 8

## 5. Assumptions

The following assumpts were made when writing the code for the auto driving car simulation project: 

### 5.1 Car movement

Assumption has been made that if a car is at either the X or Y limits of the grid, it will NOT MOVE forward. However it can STILL ROTATE either left or right, and hence will continue with the iteration and will NOT be removed for the cars deque.

This has been tested using `test_simulation[one_car_in_grid_border]` in `tests/test_simulation.py` file.


### 5.2 Number of cars in a collision

Assumption has been made that a car can collide with MORE THAN ONE car, and to update the collision info for the car with all other car names. 

This has been tested using `test_simulation[three_cars_1]` and `test_simulation[three_cars_2]` in `tests/test_simulation.py` file.


## 6. Improvements

### 6.1. Simulation workflow

If the grid has just been initialized, the options menu below: 

```
Please choose from the following options:
[1] Add a car to field
[2] Run simulation
```

Will be SKIPPED and user will be asked to enter the car name instead: 

```
Please enter the name of the car:
```

This is to avoid the scenario when the user chooses 2 to run the simulation when there are no cars in the grid. 

### 6.2. Input validation. 

Input validation has been implemented for every input. Below is a list of all the input validations, and the corresponding error statement: 

#### 1. Grid intialization

    Test invalid inputs for Grid field
    e.g. "101" 
    Test file: tests/test_grid_initialization.py
    Test name: invalid_grid

#### 1. Car input validations

    Test car unique name (Car A already exists)
    e.g. "A" 
    Test file: tests/test_car_validation.py
    Test name: valid_name, invalid_name

#### 2. Car x y direction
    
    Test car x y direction (Grid dimensions are 10 x 10)
    e.g. "1 24 N" , "1 2 U"
    Test file: tests/test_car_validation.py
    Test names: valid_x_y_direction, invalid_y, invalid_direction

#### 3. Options validation

    Test valid choice selection (Available options are 1 or 2)
    e.g. "3" 
    Test file: tests/test_options_validation.py
    Test names: options_set_valid, options_set_invalid, post_sim_options_valid, post_sim_options_invalid

## 7. Supporting documents

I have added additional notes and flowcharts to represent the simulation workflow as it helped me to understand the assignment before implementing the code. 

*simulation flowchart*: 
`docs/auto_driving_flowchart.pdf`

*Thought process notes during code implementation*: 
`docs/notes.md`


