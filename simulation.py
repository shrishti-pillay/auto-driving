from collections import defaultdict

MIN_X = 0
MIN_Y = 0

# map moves to angle of rotation of car
ANGLE = {
    'L':-90,
    'R':90
}

# map of angle to movement along X/Y axis
MOVEMENT = {
    0:{
        'axis':'y',
        'F':1,
        'direction':'N'
    },
    90:{
        'axis':'x',
        'F':1,
        'direction':'E'
    },
    270:{
        'axis':'x',
        'F':-1,
        'direction':'W'
    },
    180:{
        'axis':'y',
        'F':-1,
        'direction':'S'
    }
}

DIRECTION = {
    'N':0,
    'E':90,
    'W':270,
    'S':180
}

def run_simulation(grid):

    cars_list = list(grid.cars)

    while cars_list:

        for car in cars_list:
            
            # get next move of the car
            move = car.get_next_move()

            # increment moves count by 1
            car.moves_count += 1

            if move in ['L','R']:
                # get angle to rotate the car
                car.angle = (car.angle + (ANGLE[move])) % 360 
                # get direction based on angle
                car.direction = MOVEMENT[car.angle]['direction']

            elif move == 'F':
                # get the axis that the car is facing towards
                axis, forward, direction = MOVEMENT[car.angle].values()

                #get new car coordinates
                new_x_coord = car.x
                new_y_coord = car.y
                if axis == 'x':
                    new_x_coord += forward
                else:
                    new_y_coord += forward
                
                # check if new coordinates are out the grid
                
                # if they are not out of range, update coordinates
                if not (new_x_coord > grid.max_x or new_y_coord > grid.max_y or new_x_coord < MIN_X or new_y_coord < MIN_Y): 

                    # update car cordinates
                    car.x = new_x_coord
                    car.y = new_y_coord

        # check if any of the cars collided
        # get all cars x,y coordinates

        # for the purpose of checking collision, we need to check with ALL other cars, if the current car has collided with them, though they may have previously collided and removed from cars_queue

        #create groupings based on the coordinates 
        car_coord_groups = defaultdict(list)
        
        for car in grid.cars:

            # remove car from cars_list if no more moves left
            if car in cars_list and car.moves_queue.empty():
                cars_list.remove(car)

            # group the cars that have the same coordinates
            car_coord_groups[(car.x,car.y)].append(car)

        if car_coord_groups:
            for coord, cars in car_coord_groups.items():  
                if len(cars) > 1:         
                    for idx,car in enumerate(cars):
                        # set collision to true
                        car.collision = True

                        # add collision info to car
                        car.collision_info = {
                            'collided_with': ', '.join([x.name for x in cars if x != car]),
                            'step':car.moves_count
                        }
                        cars_list.remove(car)

    # Show result after simulation
    print('\nAfter simulation, the result is:') 

    for car in grid.cars:
        if car.collision == True:
            print(f"- {car.name}, collides with {car.collision_info['collided_with']} at {car.x, car.y} at step {car.collision_info['step']}")
        else:
            print(f" - {car.name}, {car.x ,car.y} {car.direction}\n")
