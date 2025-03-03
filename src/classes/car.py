from queue import Queue, Empty
from dataclasses import dataclass, field


@dataclass
class Car:
    """
    Represents a car in an Auto Driving Simulation.

    Attributes:
        name (str): The name of the car.
        x (int): Current x-coordinate.
        y (int): Current y-coordinate.
        direction (str): The direction the car is facing.
        angle (int): Angle of the car (0-360 degrees).
        moves (str): String representing the moves.
        moves_queue (Queue): Queue of moves for the simulation.
        moves_count (int): Index of the move at any instance.
        collision (bool): True if a collision has occurred.
        collision_info (dict): Stores details about collisions.
    """

    name: str
    x: int = 0
    y: int = 0
    direction: str = "N"
    angle: int = 0
    moves: str = field(default_factory=str)  # Ensure moves is always a string
    moves_queue: Queue = field(init=False)  # Exclude from dataclass init
    moves_count: int = 0
    collision: bool = False
    collision_info: dict = field(default_factory=dict)

    def __post_init__(self):
        """Initialize the moves queue after object creation."""
        self.moves_queue = Queue()
        self.set_moves_queue()

    def __str__(self):
        return f"Car({self.name}, Position=({self.x}, {self.y}), Direction={self.direction}, Moves={self.moves})"

    def set_moves_queue(self):
        """Creates the moves queue."""
        for move in self.moves:
            self.moves_queue.put(move)

    def get_next_move(self):
        """Returns the next move or None if queue is empty."""
        try:
            return self.moves_queue.get_nowait()
        except Empty:
            return None
