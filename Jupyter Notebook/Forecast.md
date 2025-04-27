Experimenting with various [p,d,q]

import pandas as pd
import numpy as np

from matplotlib import pyplot as plt
from datetime import date,timedelta


df = pd.read_csv('At_Gas.csv', parse_dates=['Dates'])
prices = df['Prices'].values
dates = df['Dates'].values
