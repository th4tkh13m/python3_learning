import random
from numpy import sqrt

class Coordinate(object):
    def __init__(self, x, y):
        """x, y are the x, y values of a point.
        x, y are floats"""
        self.x = x
        self.y = y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y

    def move(self,x, y):
        """x, y are floats"""
        return Coordinate(self.x + x, self.y + y)

    def getDistance(self, other):
        """Other is a coordinate of another point.
        Return the distance between 2 Coordinates"""
        return sqrt((self.getX() - other.getX())**2 + (self.getY() - other.getY())**2)

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

    def __repr__(self):
        return self.__str__()


class Field(object):
    def __init__(self):
        """Represent a dictionary of drunks"""
        self.drunks = {}

    def addDrunk(self, drunk, loc):
        """Add a drunk to the dictionary.
        drunk has the Drunk type, loc is Coordinate type. 
        Raise a Value Error if the added drunk is duplicated."""
        if drunk not in self.drunks:
            self.drunks[drunk] = loc
        else:
            raise ValueError("Duplicate drunk!")

    def moveDrunk(self, drunk):
        """Move the chosen drunk in a random direction"""
        if drunk not in self.drunks:
            raise ValueError(f"{drunk} is not in the dictionary!")
        else:
            x, y = drunk.takeStep()
            self.drunks[drunk] = self.drunks[drunk].move(x, y)

    def getLoc(self, drunk):
        """Return the Location of a Drunk"""
        if drunk in self.drunks:
            return self.drunks[drunk]
        else:
            raise ValueError(f"{drunk} is not in the dictionary!")

class Drunk():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        if self.name != None:
            return self.name
        return 'Anonymous'


class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0, 1), (-1, 0), (1, 0), (0, -1)]
        return random.choice(stepChoices)


class MasochisticDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0, -1.1), (0, 0.9), (1, 0), (-1, 0)]
        return random.choice(stepChoices)






