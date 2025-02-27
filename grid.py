from car import Car

class Grid():

    def __init__(self, max_x, max_y):
        self._max_x = max_x,
        self._max_y = max_y
        self._cars = []

    def __str__(self):
        return f'{self._max_x},{self._max_y}'

    def add_cars(self, car:Car):
        self._cars.append(car)

    @property
    def cars(self):
        return self._cars
    
    def reset_grid(self):
        self._cars = []