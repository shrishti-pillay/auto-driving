from queue import Queue

class Car():
    '''
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
    
    '''

    ''' Getters and Setters '''

    def __init__(self, name: str):
        '''Name is required for Car entity'''
        self._name = name
        self._collision = False

    def __str__(self):
        return f'Name: {self._name}, \
                  X,Y: ({self._x}, {self._y}), \
                  Direction: {self._direction}'

    @property
    def name(self):
        '''Getter for name'''
        return self._name
    
    @property
    def x(self):
        '''Getter for x pos'''
        return self._x

    @x.setter
    def x(self, x):
        '''Setter for x pos'''
        self._x = x

    @property
    def y(self):
        '''Getter for y pos'''
        return self._y

    @x.setter
    def y(self, y):
        '''Setter for y pos'''
        self._y = y

    @property
    def direction(self):
        '''Getter for direction'''
        return self._direction
    
    @direction.setter
    def direction(self, direction:str):
        '''Setter for direction'''
        self._direction = direction

    @property
    def angle(self):
        '''Getter for angle'''
        return self._angle
    
    @angle.setter
    def angle(self, angle: int):
        '''Setter for angle'''
        self._angle = angle

    @property
    def moves(self):
        '''Getter for moves'''
        return self._moves
    
    @moves.setter
    def moves(self, moves: str):
        '''Setter for moves'''

        # Create fifo queue
        moves_queue = Queue()
        for move in moves:
            Queue.put(move)

        self._moves = moves_queue

    @property
    def collision(self):
        '''Getter for collision'''
        return self._collision
    
    @collision.setter
    def collision(self):
        '''Setter for collision'''
        self._collision = False

    @property
    def collision_info(self):
        '''Getter for collision_info'''
        return self._collision_info
    
    @collision_info.setter
    def collision_info(self, collision_info: str):
        '''Setter for collision_info'''
        self._collision = collision_info

    '''Methods'''

    def get_next_move(self):
        '''Get next move for the car'''
        # Raise queue.Empty if queue is empty
        try:
            next_move = self._moves.get(block=False, timeout = 0)
        except Queue.Empty:
            self._moves.shutdown()
            return '0'
        return next_move
    
    def validate_coordinates(
            self, 
            min_x: int, 
            min_y: int, 
            max_x: int, 
            max_y: int
        ):
        ''' Validate the current car co0rdinates 
            after every move '''

        if (self._x >= min_x) and (self._y >= min_y) and \
            (self._x <= max_x) and (self._y <= max_y):
            return True
        return False
    

                                        

    

    
    


    

    


    



    
