import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


# plotting the time series data to visualize the trends or patterns
#plt.fig(figsize=(10, 6))

data = pd.read_csv('D:\Power BI thing\Forage Data sets\JPMC Data analyst\At_Gas.csv')

data['Dates'] = pd.to_datetime(data['Dates'])
data.info()


plt.scatter(data.Dates, data.Prices)
plt.grid
#plt.show()


data['Dates'] = data['Dates'].map(pd.Timestamp.toordinal)
print(data)

def loss_function(m,b,points):
    total_error = 0
    for i in range(len(points)):
        x = points.iloc[i].Dates
        y = points.iloc[i].Prices
        total_error += (y - (m* x + b)) ** 2
    total_error/float(len(points))

def gradient_descent(m_now,b_now, points, L):
    m_gradient = 0
    b_gradient = 0

    n = len(points)

    for i in range(n):
        x = points.iloc[i].Dates
        y = points.iloc[i].Prices
        m_gradient += -(2/n) * x * (y - (m_now * x + b_now))
        b_gradient += -(2/n) * (y - (m_now * x + b_now))
    
    m = m_now - m_gradient * L
    b = b_now - b_gradient * L
    return m,b

m = 0
b = 0

L = 0.0001
epoch = 300

for i in range(epoch):
    m,b = gradient_descent(m,b,data, L)

print(m,b)

plt.scatter(data.Dates , data.Prices)
