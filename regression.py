import warnings
warnings.filterwarnings('ignore')
 
 # Import libraries
import pandas as pd
import numpy as np
import quandl as quandl
import math

#Get data set
data = quandl.get('WIKI/GOOGL')

# Display first 5 records to see the picture of our data set and Feautures
print(data.head)
print(data.columns)

df = data[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]

# Volatility: relationship between High and Low
# up or low by how much: relationship between open and close
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close'])/ df['Adj. Close'] * 100.0
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open'])/ df['Adj. Open'] * 100.0

# Select the only feautures we care about
df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]
print(df.head(10))
# feature and label
forecast_col = 'Adj. Close'
df.fillna(-99999, inplace=True)
# instead of get rid of data, replace nans by outliers


forecast_out = int(math.ceil(0.01*len(df)))
print(forecast_out)
# we are using data from 10 days ago to predict the forecast ...feel free to change ...

df['label'] = df[forecast_col].shift(-forecast_out)
df.dropna(inplace=True)
print(df.head(5))