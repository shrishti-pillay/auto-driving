import queue
from queue import Queue


class Car:
    """
    A class representing the car in the Auto Driving Simulation.

    Attributes:
    -----------
    name: str
        The name of the car
    pos: tuple
        The current x, y corrdinates of the car
    direction: str
        The direction that the car is facing.
    angle: int
        Angle of the car based on the direction
        Ranges from 0 to 360
    moves: queue
        The list of moves for the simulation for the car across the grid

    """

    """ Getters and Setters """

    def __init__(self, name: str):
        """Name is required for Car entity"""
        self._name = name
        self._x = 0
        self._y = 0
        self._angle = 0
        self._direction = ''
        self._moves = ""
        self._moves_count = 0
        self._collision = False
        self._collision_info = {}

    def __str__(self):
        return f"Name: {self._name}, X,Y: ({self._x}, {self._y}), Direction: {self._direction}, Moves: {self._moves}\n"

    @property
    def name(self):
        """Getter for name"""
        return self._name

    @property
    def x(self):
        """Getter for x pos"""
        return self._x

    @x.setter
    def x(self, x):
        """Setter for x pos"""
        self._x = int(x)

    @property
    def y(self):
        """Getter for y pos"""
        return self._y

    @y.setter
    def y(self, y):
        """Setter for y pos"""
        self._y = int(y)

    @property
    def direction(self):
        """Getter for direction"""
        return self._direction

    @direction.setter
    def direction(self, direction: str):
        """Setter for direction"""
        self._direction = direction

    @property
    def angle(self):
        """Getter for angle"""
        return self._angle

    @angle.setter
    def angle(self, angle: int):
        """Setter for angle"""
        self._angle = angle

    @property
    def moves(self):
        """Getter for moves"""
        return self._moves

    @property
    def moves_queue(self):
        """Getter for moves queue"""
        return self._moves_queue

    @moves.setter
    def moves(self, moves: str):
        """Setter for moves and moves queue"""

        self._moves = moves

        # Add a fifo queue to car for commands list
        moves_queue = Queue()
        for move in moves:
            moves_queue.put(move)

        self._moves_queue = moves_queue

    @property
    def moves_count(self):
        """Getter for collision"""
        return self._moves_count

    @moves_count.setter
    def moves_count(self, moves_count):
        """Setter for collision"""
        self._moves_count = moves_count

    @property
    def collision(self):
        """Getter for collision"""
        return self._collision

    @collision.setter
    def collision(self, collision):
        """Setter for collision"""
        self._collision = collision

    @property
    def collision_info(self):
        """Getter for collision_info"""
        return self._collision_info

    @collision_info.setter
    def collision_info(self, collision_info: str):
        """Setter for collision_info"""
        self._collision_info = collision_info

    """Methods"""

    def get_next_move(self):
        try:
            return self._moves_queue.get_nowait()
        except:
            return None

    def validate_coordinates(self, min_x: int, min_y: int, max_x: int, max_y: int):
        """Validate the current car coordinates
        after every move"""

        if (
            (self._x >= min_x)
            and (self._y >= min_y)
            and (self._x <= max_x)
            and (self._y <= max_y)
        ):
            return True
        return False
