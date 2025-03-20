import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('D:\Power BI thing\Forage Data sets\JPMC Data analyst\At_Gas.csv')

#Convert to ordinal/datetime so python can read it as date, Not like incel Excel
data['Dates'] = pd.to_datetime(data['Dates'])
data['Dates'] = data['Dates'].map(pd.Timestamp.toordinal)
print(data)

#plt.scatter(data.Dates, data.Prices)
#plt.grid

plt.plot(data['Dates'],data['Prices'])
plt.grid(color='b', linestyle=':', linewidth=1)
plt.title('Time Series Data')
plt.xlabel('Date')
plt.ylabel('Value')
plt.show()

from statsmodels.tsa.stattools import adfuller

result = adfuller(data['Dates']) 
print('ADF Statistic:', result[0])
print('p-value:', result[1])
