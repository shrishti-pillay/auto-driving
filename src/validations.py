
INVALID_GRID_DIMENSIONS = 'Invalid input. Grid coordinates must be greter than 0.\n'
INVALID_CAR_COORDINATES = 'Invalid input. Car coordinates must be within the grid\n'
INVALID_CAR_NAME = 'Invalid input. Car name must be unique. Please try again.\n'
INVALID_CAR_X_Y = 'Invalid input. Car coordinates must be positive integers\n'
INVALID_CAR_DIRECTION = 'Invalid input. Car direction must be either N, S E or W.\n'
INVALID_CAR_COMMANDS = 'Invalid input. Commands must be either F, L or R\n'
DEFAULT_ERROR_MSG = "Invalid input. Please try again\n"

def get_valid_input(prompt: str, validation_func, split_count: int = 2, *args, **kwargs) -> list:
    """Prompts the user for input and validates it using the given function."""
    
    while True:
        
        if split_count > 1:
            user_input = input(prompt).split(" ")
        else: 
            user_input = [input(prompt)]

        if len(user_input) == split_count:
            validation_result = validation_func(*user_input, *args, **kwargs)
            if validation_result.get('result'):
                return user_input
            else: 
                print(validation_result.get('msg', DEFAULT_ERROR_MSG))
        else:
            print(DEFAULT_ERROR_MSG)


def validate_grid_dimensions(x: str, y: str) -> dict:
    """Validates that grid dimensions are positive integers."""
    try:
        x, y = int(x), int(y)
        if x > 0 and y > 0:
            return {'result':True}
    except ValueError:
        return {'result':False, 'msg':INVALID_GRID_DIMENSIONS}


def validate_coordinates(x: int, y: int, max_x: int, max_y: int) -> dict:
    """Validates if the given coordinates are within the grid boundaries."""
    if x > max_x or y > max_y or x < 0 or y < 0:
        return False
    return True

def validate_car_name(name: str, names: list = []) -> dict:
    """Validates that the car name is unique"""

    # if the grid already has cars, then check if the name is unique
    if names: 
        if name not in names: 
            return {'result':True}
        else: return {'result':False, 'msg': INVALID_CAR_NAME}
    else:
        # no validation required for first car
        return {'result':True}
    
def validate_car_x_y_direction(
    x: str, y: str, direction: str, max_x: int, max_y: int
) -> dict:
    """Validates car's x, y position and direction."""
    try:
        x, y = int(x), int(y)
    except ValueError:
        return {'result':False, 'msg': INVALID_CAR_X_Y}

    if not validate_coordinates(x, y, max_x, max_y):
        return {'result': False, 'msg': INVALID_CAR_COORDINATES}

    if direction not in ["N", "S", "E", "W"]:
        return {'result':False, 'msg': INVALID_CAR_DIRECTION}
    
    return {'result':True}


def validate_car_commands(commands: str) -> dict:
    """Validates car movement commands (only 'F', 'L', 'R' allowed)."""
    if [x for x in commands if x not in ["F", "L", "R"]]:
        return {'result':False, 'msg': INVALID_CAR_COMMANDS}
    return {'result':True}


def validate_options_set(prompt: str, options_set: dict) -> None:
    """Validates user choice and executes the corresponding function."""
    while True:
        choice = input(prompt)
        if choice in options_set:
            func, kwargs = options_set[choice].values()
            if kwargs: return func(kwargs)
            else: return func()
        else:
            print("Invalid choice. Please try again\n")
