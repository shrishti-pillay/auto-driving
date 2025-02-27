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

Global variables will be:
1. Grid coordinates:
- (0,0) (max_x, max_y)
2. List of car names according to order: 
- e.g. [A, B, C] 

*Car entity attributes*
1. name
2. pos -> x, y coordinates.
3. direction: current direction that the car is facing.
4. angle: angle of the direction. 
5. list of moves -> FIFO queue - can vary for each car, no limitations of length.

*Mapping each possible direction to X/Y axis and angle*
1. N = along Y axis , Forward = + 1, 0 degrees
2. E  = along X axis , Forward = + 1, 90 degrees
3. W = along X axis, Forward = -1 , 270 degrees
4. S = along Y axis, Forward = -1, 180 degrees

```
While len(car_names_list) > 0:
    For each car:
        - curr_pos =( (x,y) , direction, angle)
        - queue.get next move
        
        if move == 'L' or move == 'R'
            - angle = (angle +/- 90) % 360
            - get direction based on angle
            - set new direction of car
        if move == 'F'
            - check if curr co-ordinates is out of 
            min and max range
                - if out of range = do nothing
            get curr direction
                - add or subtract 1  from X/ Y axis accordingly
                based on direction.
            check if any of the cars collided
                - check if coordinates match with the other cars
                in the list of car names
                    if yes, then
                        - add collision information to car
                        entities affected
                        - remove the collided cars from the list
                        of car names
```

## Implementation of the Code

1. Create Car entity 
