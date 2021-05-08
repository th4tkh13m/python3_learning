from Classes import *
import random
import pylab


def randomWalk(f, d, numSteps):
    """Assumes: f a Field, d a Drunk in f, and numSteps an int >= 0.
       Moves d numSteps times, and returns the distance between
       the final location and the location at the start of the 
       walk."""
    current_loc = f.getLoc(d)
    for step in range(numSteps):
        f.moveDrunk(d)
    return current_loc.getDistance(f.getLoc(d))

def simWalks(numSteps, numTrials, dClass):
    """Assumes numSteps an int >= 0, numTrials an int > 0,
         dClass a subclass of Drunk
       Simulates numTrials walks of numSteps steps each.
       Returns a list of the final distances for each trial"""
    distances = []
    huy = dClass('Huy')
    origin = Coordinate(0, 0)
    for count in range(numTrials):
        field = Field()
        field.addDrunk(huy, origin)
        distances.append(round(randomWalk(field, huy, numSteps), 1))
    return distances

def drunkTest(walkLengths, numTrials, dClass, toPrint = True):
    """Assumes walkLengths a sequence of ints >= 0
         numTrials an int > 0, dClass a subclass of Drunk
       For each number of steps in walkLengths, runs simWalks with
         numTrials walks and prints results"""
    mean_dis = []
    max_dis = []
    min_dis = []
    for length in walkLengths:
        distances = simWalks(length, numTrials, dClass)
        mean_dis.append(round(sum(distances)/len(distances), 4))
        max_dis.append(max(distances))
        min_dis.append(min(distances))
        if toPrint:
            print(dClass.__name__, 'random walk of', length, 'steps')
            print('Mean = ', round(sum(distances)/len(distances), 4))
            print('Max = ', max(distances))
            print('Min = ', min(distances))
    return (mean_dis, max_dis, min_dis)


def plotTrend(dClass, walkLengths, numTrials):
    mean_dis, max_dis, min_dis = drunkTest(walkLengths, numTrials, dClass)
    pylab.figure('mean distance')
    pylab.xlabel('Number of Steps')
    pylab.ylabel('Distance from the origin')
    pylab.plot(walkLengths, mean_dis, label = dClass.__name__)
    pylab.plot(walkLengths,[numSteps**(1/2) for numSteps in walkLengths], 'r--', label = 'sqrt(steps)')
    pylab.xscale('log')
    pylab.yscale('log')
    pylab.legend(loc = 'upper left')
    pylab.title('Mean Distance from Origin (100 Trials)')
    pylab.show()

def simAll(drunkKinds, walkLengths, numTrials):
    for dClass in drunkKinds:
        plotTrend(dClass, walkLengths, numTrials)


if __name__ == '__main__':
    plotTrend(UsualDrunk, (10, 100, 1000, 10000), 100)

