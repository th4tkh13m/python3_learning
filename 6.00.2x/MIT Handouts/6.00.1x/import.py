import pylab as plt
import math

mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []
for i in range(0, 30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(1.5**i)

plt.figure('lin')
plt.xlabel('sample points')
plt.ylabel('linear function')
plt.title('Linear')
plt.ylim(0,1000)
plt.plot(mySamples, myLinear)
plt.figure('quad')
plt.plot(mySamples, myQuadratic)
plt.figure('cube')
plt.plot(mySamples, myCubic)
plt.figure('expo')
plt.title('Exponential')
plt.ylim(0,1000)
plt.plot(mySamples, myExponential)
plt.figure('quad')

plt.ylabel('quadratic function')

plt.show()