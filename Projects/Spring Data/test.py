import pylab
import numpy as np


def loadData():
    """Load the experimental spring data.
    Returns the distances of the spring and the masses of the weight""" 
    distances = []
    masses = []
    data = open('springData.txt')
    for line in data:
        try:
            distances.append(float(line.split()[0]))
            masses.append(float(line.split()[1]))
        except ValueError:
            continue
    return distances, masses

def linearRegression(distances, forces, verbose = True):
    """Graph the data points and using Least Square Method,
    calculate the Linear and Quadratic Regression, and plot them besides the points.
    Returns the values of the linear and quadratic formula."""
    model1 = pylab.polyfit(forces, distances, 1)
    model2 = pylab.polyfit(forces, distances, 2)
    yVals_1 = pylab.polyval(model1, forces)
    yVals_2 = pylab.polyval(model2, forces)
    if verbose:
        pylab.plot(forces, distances, 'ko')
        pylab.xlabel('Force (N)')
        pylab.ylabel('Distance (m)')
        pylab.plot(forces, yVals_1, label = 'Linear Regression')
        pylab.plot(forces, yVals_2, label = 'Quadratic Regression')
        pylab.legend(loc = 'best')
        pylab.show()
    return yVals_1, yVals_2

def aveMeanSquareError(data, predicted):
    """Given the data and predicted data, returns the average
    mean square error"""
    error = 0.0
    for i in range(len(data)):
        error = error + (data[i] - predicted[i])**2
    return error / len(data)



####TESTING####
distances, masses = loadData()
forces = np.array(masses)*9.8
distances = np.array(distances)
yLinear, yQuadratic = linearRegression(distances, forces, False)
print(aveMeanSquareError(distances, yLinear))
print(aveMeanSquareError(distances, yQuadratic))