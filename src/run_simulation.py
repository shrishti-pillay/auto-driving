from collections import defaultdict
from validations import validate_coordinates

# Map moves to angle of rotation of car
ANGLE = {"L": -90, "R": 90}

# Map of angle to movement along X/Y axis
MOVEMENT = {
    0: {"axis": "y", "F": 1, "direction": "N"},
    90: {"axis": "x", "F": 1, "direction": "E"},
    270: {"axis": "x", "F": -1, "direction": "W"},
    180: {"axis": "y", "F": -1, "direction": "S"},
}

# Map of Direction to Angle
DIRECTION = {"N": 0, "E": 90, "W": 270, "S": 180}


def run_simulation(grid) -> None:
    """Runs the car movement simulation on the grid."""

    # Create list of cars
    cars_list = list(grid.cars)

    while cars_list:
        for car in cars_list:
            # Get next move of the car
            move = car.get_next_move()

            if move is None:
                continue  # Skip if no moves left

            # Increment moves count by 1
            car.moves_count += 1

            if move in ANGLE:
                # Update car's angle and direction
                car.angle = (car.angle + ANGLE[move]) % 360
                car.direction = MOVEMENT[car.angle]["direction"]

            elif move == "F":
                # Get movement details
                axis, forward, _ = MOVEMENT[car.angle].values()

                # Calculate new coordinates
                new_x, new_y = car.x, car.y
                if axis == "x":
                    new_x += forward
                else:
                    new_y += forward

                # Validate new coordinates within grid boundaries
                result = validate_coordinates(new_x, new_y, grid.max_x, grid.max_y).get('result', False)
                if result:
                    car.x, car.y = new_x, new_y

        # Check for collisions
        car_coord_groups = defaultdict(list)
        for car in grid.cars:
            # Group cars by coordinates
            car_coord_groups[(car.x, car.y)].append(car)

        # Process collisions
        for cars in car_coord_groups.values():
            if len(cars) > 1:
                for car in cars:
                    if car in cars_list:
                        car.collision = True
                        car.collision_info = {
                            "collided_with": ",".join(
                                [x.name for x in cars if x != car]
                            ),
                            "step": car.moves_count,
                        }
                        cars_list.remove(car)
                        
        # remove car if there are no more moves
        for car in grid.cars:
            if car in cars_list and car.moves_queue.empty():
                cars_list.remove(car)

    # Display simulation results
    print("After simulation, the result is:")
    for car in grid.cars:
        if car.collision:
            print(
                f"- {car.name}, collides with {car.collision_info['collided_with']} at ({car.x},{car.y}) at step {car.collision_info['step']}"
            )
        else:
            print(f"- {car.name}, ({car.x},{car.y}) {car.direction}")
