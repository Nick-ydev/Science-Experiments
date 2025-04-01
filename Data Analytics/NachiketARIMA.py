import numpy as np
import pandas as pd
from matplotlib import pyplot
from statsmodels.tsa.ar_model import AutoReg

# df = pd.read_csv('D:\Power BI thing\Forage Data sets\JPMC Data analyst\At_Gas.csv',index_col=0,parse_dates=True)
# X = df.values
# print('Shape of Data \t',df.shape)
# print('original Dataset:\n',df.head)
# print('After extraxting: \n', X)

# df.plot

for month in range(0,13):
    print (month, "bf4")
    month = ((month + 1) % 12) or 12 # 1 or 12 > 1
    print (month, "after")
    if month == 1:
        month =+ 1
    
