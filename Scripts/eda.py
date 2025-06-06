import pandas as pd
def count_occur(df,columns):
  return df[columns].value_counts()

def change_to_date(df):
  df["date"]=pd.to_datetime(df["date"],format='ISO8601')
  return df


#decompose the data
def decompose_data(df):
 import matplotlib.pyplot as plt 
 from statsmodels.tsa.seasonal import seasonal_decompose
 decomposition = seasonal_decompose(df['Headlines'], model='additive', period=4)
 plt.figure(figsize=(14,6))
 plt.plot(df['Headlines'], label='Original')
 plt.legend()
 plt.show()
 plt.figure(figsize=(14,6))
 plt.plot(decomposition.seasonal, label='Seasonal')
 plt.legend()
 plt.show()
 plt.figure(figsize=(14,6))
 plt.plot(decomposition.trend, label='Trend')
 plt.legend()
 plt.show()
 plt.figure(figsize=(14,6))
 plt.plot(decomposition.resid, label='Irregular')
 plt.legend()
 plt.show()