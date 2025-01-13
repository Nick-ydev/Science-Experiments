import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv

data = pd.read_csv('D:\Power BI thing\Forage Data sets\JPMC Data analyst\At_Gas.csv')
#data['Dates'] = data.index
data['Dates'] = pd.to_datetime(data['Dates'])
data['Dates'] = data['Dates'].map(pd.Timestamp.toordinal)

# Read the CSV file (replace 'data.csv' with your file path)
with open('D:\Power BI thing\Forage Data sets\JPMC Data analyst\At_Gas.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header row
    data = np.array(list(reader), dtype=int)

# Calculate column averages
age_avg = np.mean(data[:, 0])  # Column 0 (Age)
salary_avg = np.mean(data[:, 1])  # Column 1 (Salary)

# Display the results
print(Average Age: {age_avg:.2f})
print(Average Salary: {salary_avg:.2f})
