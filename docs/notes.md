# Documentation of the thought process

## Purpose
The purpose of this document is to record my though process while implemting this auto driving car simulation. 

## Thought Process

### Recording possible inputs accepted by the program

1. Width and Height (dimensions)
    - bottom left = 0,0
    - top right = 9,9
2. One or more cars withthe following details: 
    - name = unique name 
    - starting position in the form of corrdinates (1,2)
    - direction that they are facing 
        N, S, E, W 
3. Movement 
    - L = Rotate left by 90 - face the left along x axis 
    - R = Rotate right by 90 - face the right along right axis 
    - F = move forward by one grid --- x or y aixis + 1

### Important things to note. 

1. The direction of the car at each point. How to record the direction at each stage. 
2. Direction of the car determines whether the move will be + or - and whether it is along x or y axis. 
3. It it reaches the borders for X or Y, it should stay at its current position. 

### Miro board flowchart

Since there is a certain flow of execution of the program, best would be to translate the flow into a flowchart diagram to understand the simulation. 


-- insert image of flowchart here 

### Alogrithm for calculating the direction and movement of the car. 


1. Order of the car must be preserved. 
- Make a list of car names: [A, B, C] based on the order of creation
2. Order of the directions must be preserved
- Implement queue to store this , follow FIFO structure

3. Create a mapping of the moves and the operations:

    L = -90 degrees

    R = +90 degrees

#### Calculating the position at every move
Order of the car must be preserved. 
Make a list of cars: [A, B, C] based on the order of creation
Order of the directions must be preserved
implement queue to store this , follow FIFO structure

Create a mapping of the moves and the operations:
L = -90 degrees
R = +90 degrees


**Calculating the position at every move
For each Car entity:
name
pos -> x, y coordinates
direction: current direction that the car is facing
angle: angle of the direction. 
list of moves -> FIFO queue - can vary for each car, no limitations of length.

** Mapping each possible direction to X/Y axis and angle
N = along Y axis , Forward = + 1, 0 degrees
E  = along X axis , Forward = + 1, 90 degrees
W = along X axis, Forward = -1 , 270 degrees
S = along Y axis, Forward = -1, 180 degrees


```python
While len(car_names_list) > 0:
    For each car:
        queue.get next move
        if move == L or move == R
            angle = (angle +/- 90) % 360
            get direction based on angle
            set new direction of car
        if move == F
            get curr direction
            add or subtract 1  from X/ Y axis accordingly based on direction.
            *if above calculation results in coordinates out of range, then nullify the calculation, keep coordinates as-is*

    After every iteration of the cars list:
        check if any of the cars collided
        for each car in grid:
            if car is in cars_list:
                check if coordinates match with the other cars in the list of car names
                if yes, then
                    set collision to true
                    add collision information to car entities affected
                    remove car from cars_list
        
        for each car in grid:
            if no moves in queue,
                remove car name from cars_list
```

## Implementation of the Code

Create Car entity , will need the following attributes

1. name
2. x - include validation  - x must be within 0 and grid.max_x
3. y - include validation  - y must be within 0 and grid.max_y
4. direction ['N', 'S', 'W', 'E'] - include validation
5. angle - to determine using the direction
6. moves 
7. moves queue (convert moves to queue)
8. collision: bool: default to False
9. collision_info: information of the collision if it occurs.

To track the cars in a simulation, we will need another entity called Grid which will consist of the list of cars in the simulation. 

This list of cars will also reflect the order that the cars were created. 

To trace the movements of each car while iterating over them, a deque can be implemented to pop the first car from the queue, then move the car, if the car has not collided if any of the other cars then the car can be added back to the car deque.

Create Grid entity with the following attributes

1. max_x
2. max_y
3. min_x = 0
4. min_y = 0


## Assumptions made during code development

1. Assumption has been made that if a car is at either the X or Y limits of the grid, it will NOT MOVE forward. However it can STILL ROTATE either left or right, and hence will continue with the iteration and will NOT be removed for the cars deque.

2. Assumption has been made that a car can collide with more than 1 car, and to update the collision info for the car will all other car names. This has been tested using test_simulation[three_cars_1] and test_simulation[three_cars_2] in tests/test_simulation.py




