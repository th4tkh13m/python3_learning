import random
import numpy as np

random.seed(0)
# def throwNeedles(numNeedles):
#     success = 0
#     for n in range(numNeedles):
#         x = random.random()
#         if (1+x)**2 < 2.0:
#             success += 1
#     sqrt2 = 1+(float(success)/numNeedles)
#     return sqrt2        

# print(throwNeedles(100000))    
# 
class Coordinate():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distance(self, coor):
        assert type(coor) == Coordinate
        return np.sqrt((self.getX() - coor.getX())**2 +\
                (self.getY() - coor.getY())**2)
    

    def __str__(self):
        return '<' + str(self.getX()) + ',' +\
                str(self.getY()) + '>'

    def __repr__(self):
        return self.__str__()
    
class Field():

    def __init__(self, side, origin):
        self.origin = origin
        self.coor = []
        self.circle = []
        self.side = side

    def addCoorInSquare(self, coor):
        if self.isInRectangle(coor):
            self.coor = self.coor +\
                        [coor]

    def randomNeedle(self):
        a = self.side
        x = random.uniform(-a, a)
        y = random.uniform(-a, a)
        coor = Coordinate(x, y)
        self.coor.append(coor)
        return coor

    def isInCircle(self, coor):
        return coor.distance(self.origin) < 1
    
    def addCoorInCircle(self, coor):
        if self.isInCircle(coor):
            self.circle.append(coor)

    def countSquare(self):
        return len(self.coor)

    def countCircle(self):
        return len(self.circle)


    

def calculatingPi(numTrials,numNeedles, origin, side = 1):
    success = 0
    sqrt_lst = []
    for trial in range(numTrials):
        f = Field(side, origin)
        for throw in range(numNeedles):
            x = f.randomNeedle()
            f.addCoorInCircle(x)
        cir = f.countCircle()
        sqr = f.countSquare()
        sqrt_lst.append(4*cir/sqr)
    return sqrt_lst
def getPi():
    origin = Coordinate(0,0)
    x = calculatingPi(50, 100000, origin)
    mean = sum(x)/len(x)
    SD = np.sqrt(sum([(y - mean)**2 for y in x ])/len(x))
    return mean, SD
m, SD = getPi()
print('Mean:', m)
print('SD:', SD)


        
        
