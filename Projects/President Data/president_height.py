import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn; seaborn.set() # set plot style

# What Is the Average Height of US Presidents?

data = pd.read_csv('president_heights.csv')
heights = np.array(data['height(cm)'])
print("\nMean height:        ", round(heights.mean(), 2))
print("Standard deviation: ", round(heights.std(),2))
print("Minimum height:     ", heights.min())
print("Maximum height:     ", heights.max())

print("\n25th percentile:   ", np.percentile(heights, 25))
print("Median:            ", np.median(heights))
print("75th percentile:   ", np.percentile(heights, 75))

plt.hist(heights)
plt.title('Height Distribution of US Presidents')
plt.xlabel('height (cm)')
plt.ylabel('number')
plt.show()