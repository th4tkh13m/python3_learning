import pylab
import random

#Pascal Problem
def simulatePascal(numTrials):
    """Simulate the Pascal problem numTrials times.
    Pascal problem: Determine whether whether or not it would be profitable
     to bet that within twenty-four rolls of a pair of dice there will be at least
     a double six"""
    count = 0
    for trial in range(numTrials):
        for roll in range(24):
            die1 = random.randint(1, 6)
            die2 = random.randint(1, 6)
            if die1 == 6 and die2 == 6:
                count = count + 1
                break
    return count/numTrials

random.seed(0)
print(simulatePascal(100000))
#Return approximately 0.49. It is a lost bet.
