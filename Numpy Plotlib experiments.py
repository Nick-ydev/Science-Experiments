import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.model_selection import train_test_split

# plotting the time series data to visualize the trends or patterns
#plt.fig(figsize=(10, 6))

data = pd.read_csv('D:\Power BI thing\Forage Data sets\JPMC Data analyst\At_Gas.csv')

plt.scatter(data.studytime, data.score)
plt.show()