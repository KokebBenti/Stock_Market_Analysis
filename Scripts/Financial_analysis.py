def load_file(ticker,suffix="_historical_data.csv"):
  import pandas as pd
  file_path=f"{ticker}{suffix}"
  df=pd.read_csv(file_path)
  df["Date"] = pd.to_datetime(df['Date'])
  df.set_index("Date", inplace=True)
  return df 

def moving_av(df,interval,title):
  df[title] = df['Adj Close'].rolling(window=interval).mean()
  return df

def calculate_rsi(df,period):
 delta = df['Adj Close'].diff()
 gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
 loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
 rs = gain / loss
 df['RSI'] = 100 - (100 / (1 + rs))  
 return df

def MACD(df): 
 sho = df['Adj Close'].ewm(span=12, adjust=False).mean()
 lon = df['Adj Close'].ewm(span=26, adjust=False).mean()
 df['MACD'] = sho - lon
 df['Signal_Line'] = df['MACD'].ewm(span=9, adjust=False).mean()