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
    moves: list
        The list of moves for the simulation for the car across the grid
    
    
    '''
    def __init__(self, name: str):
        '''Name is required for Car entity'''
        self.name = name

    @property
    def name(self):
        '''Getter for name'''
        return self._name
    
    @property
    def pos(self):
        '''Getter for pos'''
        return (self._x, self._y)

    @pos.setter
    def pos(self, pos:tuple):
        '''Setter for pos'''
        self._x , self._y = pos

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
    def moves(self, moves):
        '''Setter for moves'''
        self._moves = moves
    

    

    


    



    
