from dataclasses import dataclass, field
from classes.car import Car

@dataclass
class Grid:
    """
    A class representing the X, Y dimensions of the grid for the simulation, and the list
    of cars included.

    Attributes:
    -----------
    max_x: int
        The max X coordinate of the grid.
    max_y: int
        The max Y coordinate of the grid.
    cars: list
        The list of Car objects in the Grid.
    """

    max_x: int
    max_y: int
    min_x: int = field(default=0, init=False)
    min_y: int = field(default=0, init=False)
    cars: list = field(default_factory=list, init=False)

    def __post_init__(self):
        """Initialize cars list."""
        self.cars = []

    def __str__(self):
        return f"{self.max_x},{self.max_y}"

    def add_cars(self, car: Car):
        """Adds a car to the grid."""
        self.cars.append(car)

    def reset_grid(self):
        """Removes all cars from the grid."""
        self.cars.clear()
