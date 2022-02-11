import warnings
warnings.filterwarnings('ignore')
 
 # Import libraries
import pandas as pd
import numpy as np
import quandl as quandl

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

print(df.head())