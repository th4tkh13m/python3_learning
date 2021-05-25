import random, pylab

# You are given this function
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)

# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    # TODO
    pylab.title(title)
    pylab.hist(values, bins = numBins)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    pylab.show()
                    
# Implement this -- Coding Part 2 of 2
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """
    # TODO
    longest_runs = []
    for trial in range(numTrials):
        longest = 1
        run = 1
        last_roll = None
        for roll in range(numRolls):
            result = die.roll()
            if last_roll == None:
                last_roll = result
                continue
            if last_roll == result:
                run = run + 1
            else:
                if run > longest:
                    longest = run
                run = 1
            last_roll = result
        if run > longest:
                longest = run
        longest_runs.append(longest)
    makeHistogram(longest_runs, 10, "Longest run", "Num occurrences")
    return round(sum(longest_runs) / numTrials,3)

random.seed(0)    
# One test case
# print(getAverage(Die([1,2,3,4,5,6,6,6,7]), 20, 2))
print(getAverage(Die([1]), 10, 1000))