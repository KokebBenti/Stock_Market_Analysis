def calculate_sentiment(df):
 from textblob import TextBlob
 return TextBlob(df).sentiment.polarity


def import_stocks(ticker,suffix="_historical_data.csv"):
  import pandas as pd
  file_path=f"{ticker}{suffix}"
  df=pd.read_csv(file_path)
  df["Date"] = pd.to_datetime(df['Date'])
  df.set_index("Date", inplace=True)
  return df 


def DR(df): 
  df['Daily Returns'] = df['Adj Close'].pct_change()
  return(df)