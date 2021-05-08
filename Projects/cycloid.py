import pylab as plt
import math

x_axis = []
y_axis = []
for i in range(401):
    x_axis.append(2*i/100*math.pi-2*math.sin(math.pi*i/100))
    y_axis.append(2-2*math.cos(math.pi*i/100))

plt.figure('cycloid')
plt.plot(x_axis, y_axis, label = 'parametric cure')
plt.legend(loc = 'upper left')
plt.title('Cycloid with 2 archs')
plt.ylim(0,30)
plt.xlim(0,30)
plt.show()
plt.ylim(3)
