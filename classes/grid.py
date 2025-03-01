from classes.car import Car


class Grid:
    '''
    A class repredenting the X , Y dimensions of the grid for the smilation, and the list 
    of cars included

    Attributes:
    -----------
    max_x: int
        The max X coordinate of the grid
    max_y: int
        The max Y coordinate of the grid
    cars: list
        The list of Car objects in the Grid

    '''

    def __init__(self, max_x: int, max_y: int):
        self._max_x = int(max_x)
        self._max_y = int(max_y)
        self._cars = []

    def __str__(self):
        return f"{self._max_x},{self._max_y}"

    def add_cars(self, car: Car):
        self._cars.append(car)

    @property
    def cars(self):
        '''Getter for cars list'''
        return self._cars
    
    @property
    def max_x(self):
        '''Getter for max_x'''
        return self._max_x
    
    @property
    def max_y(self):
        '''Getter for max_y'''
        return self._max_y

    def reset_grid(self):
        self._cars = []
