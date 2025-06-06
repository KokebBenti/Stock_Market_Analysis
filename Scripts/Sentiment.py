def pick_stock(df,ticker):
  import pandas as pd
  dfst=df[df['stock'] == ticker]
  dfst.set_index('date', inplace=True)
  dfst.index = pd.to_datetime(dfst.index,format='ISO8601')
  dfst.index = dfst.index.tz_localize(None)
  return dfst