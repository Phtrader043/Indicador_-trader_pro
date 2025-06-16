import pandas as pd
import ta

def calcular_indicadores(df):
    df['rsi'] = ta.momentum.RSIIndicator(close=df['close']).rsi()
    macd = ta.trend.MACD(close=df['close'])
    df['macd'] = macd.macd_diff()
    df['ema'] = ta.trend.EMAIndicator(close=df['close'], window=9).ema_indicator()
    df['adx'] = ta.trend.ADXIndicator(high=df['high'], low=df['low'], close=df['close']).adx()
    bollinger = ta.volatility.BollingerBands(close=df['close'])
    df['bollinger_width'] = bollinger.bollinger_hband() - bollinger.bollinger_lband()
    df['stochastic'] = ta.momentum.StochasticOscillator(high=df['high'], low=df['low'], close=df['close']).stoch()
    return df