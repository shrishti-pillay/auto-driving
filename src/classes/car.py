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
    moves_count: int
        Index of the move at any instance of the simulation
    collision: bool
        Attribute is set to True if a collision has occured.
        Default value is False
    collision_info: dict
        Collision information of which car the car collided with
        Fields:
            'collided_with': Name of the other car
            'step': moves_count value at the point of collision

    Methods:
    ---------
    get_next_move()
        returns the next element in moves queue if its not empty
        returns None if moves queue is empty
    """

    """ Getters and Setters """

    def __init__(
        self,
        name: str,
        x: int = 0,
        y: int = 0,
        direction: str = "N",
        angle: int = 0,
        moves: str = "",
    ):
        """Name is required for Car entity"""
        self._name = name
        self._x = x
        self._y = y
        self._direction = direction
        self._angle = angle
        self._moves = moves

        # create a fifo queue for moves
        self._moves_queue = Queue()
        for move in moves:
            self._moves_queue.put(move)

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

    @property
    def moves_count(self):
        """Getter for moves_count"""
        return self._moves_count

    @moves_count.setter
    def moves_count(self, moves_count):
        """Setter for moves_count"""
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
