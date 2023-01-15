from candlestick import candlestick
import plotly.graph_objects as go
from datetime import datetime
import pandas as pd
import requests
candles_df=pd.read_csv(r"file://DESKTOP-EBL9OR0/Users/Manisha/Downloads/Sample.csv")

candles_df['Timestamp']=pd.to_datetime(candles_df['Timestamp'])
candles_df.set_index('Timestamp',inplace=True)
candles_df['return']=candles_df['Close'].pct_change()
candles_df.dropna(inplace=True)
print(candles_df)
dfpl = candles_df[0:3000]


fig = go.Figure(data=[go.Candlestick(x=dfpl.index,
                open=dfpl['Open'],
                high=dfpl['High'],
                low=dfpl['Low'],
                close=dfpl['Close'])])

fig.show()

target = 'BullishRisingThree'
candles_df_BullishRisingThree = candlestick.bullish_rising_three(candles_df, target=target)
print("\n\n ***************************** Following are the occurence of ",target," *****************************\n\n")
print("Total occurence of ",target," ",candles_df_BullishRisingThree[candles_df_BullishRisingThree[target] == True].shape[0])
print("\n\n")
print(candles_df_BullishRisingThree[candles_df_BullishRisingThree[target] == True])

target = 'BearishfallingThree'
candles_df_BearishfallingThree = candlestick.bearish_falling_three(candles_df, target=target)
print("\n\n ************** Following are the occurence of ",target," **************\n\n")
print("Total occurence of ",target," ",candles_df_BearishfallingThree[candles_df_BearishfallingThree[target] == True].shape[0])
print("\n\n")
print(candles_df_BearishfallingThree[candles_df_BearishfallingThree[target] == True])

target='Bearishengulfing'
candles_df_Bearishengulfing= candlestick.bearish_engulfing(candles_df,target=target)
print("\n\n ******************** Following are the occurence of ",target," ****************\n\n")
print("Total occurence of ",target," ",candles_df_Bearishengulfing[candles_df_Bearishengulfing[target] == True].shape[0])
print("\n\n")
print(candles_df_Bearishengulfing[candles_df_Bearishengulfing[target] == True])

target='Bullishengulfing'
candles_df_Bullishengulfing = candlestick.bullish_engulfing(candles_df,target=target)
print("\n\n ********************** Following are the occurence of ",target," ******************\n\n")
print("Total occurence of ",target," ",candles_df_Bullishengulfing[candles_df_Bullishengulfing[target] == True].shape[0])
print("\n\n")
print(candles_df_Bullishengulfing[candles_df_Bullishengulfing[target] == True])