import random
random.seed(0)

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    # Your code here
    count = 0
    for trial in range(numTrials):
        balls = [0,0,0,1,1,1] #Red is 0, Green is 1
        choose = []
        for turn in range(3):
            pick = random.choice(balls)
            choose.append(pick)
            balls.remove(pick)
        if set(choose) == {0} or set(choose) == {1}:
            count = count + 1
    return count/numTrials

print(noReplacementSimulation(1000))

def calculateIntegration(f, a, b, numSteps):
    xVals, yVals = [], []
    xVal = a
    step = (a - b)/numSteps
    while xVal <= b:
        xVals.append(xVal)
        yVals.append(f(xVal))
        xVal = xVal + step
    max
    xUnders, yUnders, xOvers, yOvers = [], [], [], []
    for i in range(len(xVals)):
        if yVals[i] <= f(xVals[i])


