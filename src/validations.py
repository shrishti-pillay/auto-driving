def get_valid_input(prompt: str, validation_func, split_count: int = 2, *args, **kwargs):
    while True:
        
        if split_count > 1:
            user_input = input(prompt).split(" ")
        else: 
            user_input = [input(prompt)]

        if len(user_input) == split_count and validation_func(*user_input, *args, **kwargs):
            return user_input
        print("Invalid input. Please try again\n")


def validate_grid_dimensions(x: str, y: str) -> bool:
    try:
        return int(x) > 0 and int(y) > 0
    except ValueError:
        return False


def validate_coordinates(x: int, y: int, max_x: int, max_y: int) -> bool:
    if x > max_x or y > max_y or x < 0 or y < 0:
        return False
    else:
        return True


def validate_car_x_y_direction(
    x: str, y: str, direction: str, max_x: int, max_y: int
) -> bool:

    try:
        x = int(x)
        y = int(y)
    except ValueError:
        return False

    if not validate_coordinates(x, y, max_x, max_y):
        return False

    if direction not in ["N", "S", "E", "W"]:
        return False
    return True


def validate_car_commands(commands):
    if [x for x in commands if x not in ["F", "L", "R"]]:
        return False
    return True


def validate_options_set(choice, options_set):
    while True:
        if choice in options_set:
            func, kwargs = options_set[choice].values()
            if kwargs: return func(kwargs)
            else: return func()
        else:
            print("Invalid choice. Please try again\n")
