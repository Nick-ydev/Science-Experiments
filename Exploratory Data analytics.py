import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

happiness_data = pd.read_csv('D:\DATA SCIENCE Experiments\Happiness Index.csv')

print(happiness_data.head())
#print(happiness_data.describe())
#print(happiness_data.isnull().sum())

duplicatesValues = happiness_data.duplicated()
print(duplicatesValues.sum())
happiness_data[duplicatesValues]

from sklearn.preprocessing import StandardScaler
stdScale = StandardScaler()
stdScale
happiness_data['Happiness Score'] = stdScale.fit_transform(happiness_data[['Happiness Score']])
happiness_data.head()