import pandas as pd
def count_occur(df,columns):
  return df[columns].value_counts()

def change_to_date(df):
  df["date"]=pd.to_datetime(df["date"],format='ISO8601')
  return df
