import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


# plotting the time series data to visualize the trends or patterns
#plt.fig(figsize=(10, 6))

data = pd.read_csv('D:\Power BI thing\Forage Data sets\JPMC Data analyst\At_Gas.csv')
#data['Dates'] = data.index
data['Dates'] = pd.to_datetime(data['Dates'])
data['Dates'] = data['Dates'].map(pd.Timestamp.toordinal)
print(data)


data.info()

plt.scatter(data.Dates, data.Prices)
plt.grid
#plt.show()


X = data[['Dates']]
y = data['Prices'] 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Initializing the linear regression model
model = LinearRegression()

# Training the model on the training data available
model.fit(X_train,  y_train)

# Making predictions on the testing data
y_pred = model.predict(X_test)

# Evaluating the models using MSE metric
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# Plotting the actual vs predicted values inorder to visualize model performance
plt.figure(figsize=(10, 6))
plt.plot(data.index, data['Prices'], label='Actual')
plt.plot(X_test.index, y_pred, label='Predicted', color='red')
plt.title('Actual vs Predicted Nat Gas')
plt.xlabel('Date')
plt.ylabel('Number of Passengers')
plt.legend()

# Saving the plot as an image
plt.savefig('actual_vs_predicted.png')
plt.show()


#plt.scatter(data.Dates , data.Prices)

#Open this code when both columns are numbers, this doesnt work with date
#Also this is the Mean Squared function done manually , 
#Placeholder#1 <Open>
# def loss_function(m,b,points):
#     total_error = 0
#     for i in range(len(points)):
#         x = points.iloc[i].Dates    
#         y = points.iloc[i].Prices
#         total_error += (y - (m* x + b)) ** 2
#     total_error/float(len(points))

# def gradient_descent(m_now,b_now, points, L):
#     m_gradient = 0
#     b_gradient = 0

#     n = len(points)

#     for i in range(n):
#         x = points.iloc[i].Dates
#         y = points.iloc[i].Prices
#         m_gradient += -(2/n) * x * (y - (m_now * x + b_now))
#         b_gradient += -(2/n) * (y - (m_now * x + b_now))
    
#     m = m_now - m_gradient * L
#     b = b_now - b_gradient * L
#     return m,b

# m = 0
# b = 0

# L = 0.0001
# epoch = 300

# for i in range(epoch):
#     m,b = gradient_descent(m,b,data, L)

# print(m,b)
#Placeholder#1 <Close>



