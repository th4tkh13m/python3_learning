import numpy as np
import pylab

def loadFile():
    inFile = open('julytemps.txt')
    high = []
    low = []
    for line in inFile:
        fields = line.split()
        if len(fields) != 3 or not fields[0].isdigit():
            continue
        else:
            high.append(int(fields[1]))
            low.append(int(fields[2]))
    return (low, high)

def plotDiff():
    highTemps, lowTemps = loadFile()
    diff = np.array(highTemps) - np.array(lowTemps)
    pylab.figure("Differences")
    pylab.title('Differences between high and low Temp')
    pylab.plot([x for x in range(1, 32)], diff, label = 'Differences in Temp')
    pylab.ylabel('Diffenrences')
    pylab.xlabel('Day in July')
    pylab.legend(loc = 'best')
    pylab.show()

plotDiff() 