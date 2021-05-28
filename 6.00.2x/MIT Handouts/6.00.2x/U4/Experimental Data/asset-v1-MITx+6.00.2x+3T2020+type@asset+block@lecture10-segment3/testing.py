import pylab
import numpy as np


def loadData():
    """Return the x and y values of the mysteryData.txt file"""
    xVals, yVals = [], []
    f = open("mysteryData.txt")
    for line in f:
        try:
            xVals.append(float(line.split()[1]))
            yVals.append(float(line.split()[0]))
        except ValueError:
            continue
    return xVals, yVals

# def rSquare1(data, predicted):
#     mean = sum(data) / len(data)
#     numerator = sum([(data[i] - predicted[i])**2 for i in range(len(data))])
#     denominator = sum([(data[i] - mean)**2 for i in range(len(data))])
#     return numerator / denominator

def rSquare2(data, predicted):
    mean = data.sum() / float(len(data))
    numerator = ((data - predicted)**2).sum()
    denominator = ((data - mean)**2).sum()
    return 1 - numerator / denominator

def Regression(xVals, yVals, degrees, verbose = True):
    yVals_predicted = {}
    for degree in degrees:
        model = pylab.polyfit(xVals, yVals, degree)
        yVals_predicted[degree] = pylab.polyval(model, xVals)
    if verbose:
        pylab.figure("Regression")
        pylab.title("Regression of various degree polynomials")
        pylab.plot(xVals, yVals, 'ko')
        pylab.xlabel("x Values")
        pylab.ylabel("y Values")
        for degree in yVals_predicted:
            pylab.plot(xVals, yVals_predicted[degree],\
                label = f"Regression degree : {degree}, R^2 = " +\
                    str(rSquare2(pylab.array(yVals), yVals_predicted[degree])))
        pylab.legend(loc = "best")
        pylab.show()
    return yVals_predicted

xVals, yVals = loadData()
print(Regression(xVals, yVals, (1, 2, 4)))
