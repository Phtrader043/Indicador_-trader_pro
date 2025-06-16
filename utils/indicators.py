import pandas as pd
import numpy as np


def calcular_ema(df, periodo=14):
    df['ema'] = df['close'].ewm(span=periodo, adjust=False).mean()
    return df


def calcular_rsi(df, periodo=14):
    delta = df['close'].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.rolling(window=periodo).mean()
    avg_loss = loss.rolling(window=periodo).mean()

    rs = avg_gain / avg_loss
    df['rsi'] = 100 - (100 / (1 + rs))
    return df


def calcular_macd(df, fast=12, slow=26, signal=9):
    ema_fast = df['close'].ewm(span=fast, adjust=False).mean()
    ema_slow = df['close'].ewm(span=slow, adjust=False).mean()

    df['macd'] = ema_fast - ema_slow
    df['macd_signal'] = df['macd'].ewm(span=signal, adjust=False).mean()
    return df


def calcular_adx(df, periodo=14):
    df['tr'] = pd.concat([
        (df['high'] - df['low']).abs(),
        (df['high'] - df['close'].shift()).abs(),
        (df['low'] - df['close'].shift()).abs()
    ], axis=1).max(axis=1)

    df['+dm'] = np.where(
        (df['high'] - df['high'].shift()) > (df['low'].shift() - df['low']),
        np.maximum((df['high'] - df['high'].shift()), 0), 0)

    df['-dm'] = np.where(
        (df['low'].shift() - df['low']) > (df['high'] - df['high'].shift()),
        np.maximum((df['low'].shift() - df['low']), 0), 0)

    tr14 = df['tr'].rolling(window=periodo).sum()
    plus_dm14 = df['+dm'].rolling(window=periodo).sum()
    minus_dm14 = df['-dm'].rolling(window=periodo).sum()

    plus_di14 = 100 * (plus_dm14 / tr14)
    minus_di14 = 100 * (minus_dm14 / tr14)
    dx = (abs(plus_di14 - minus_di14) / (plus_di14 + minus_di14)) * 100
    df['adx'] = dx.rolling(window=periodo).mean()

    df.drop(['tr', '+dm', '-dm'], axis=1, inplace=True)
    return df


def calcular_bollinger_bands(df, periodo=20):
    df['bb_middle'] = df['close'].rolling(window=periodo).mean()
    df['bb_std'] = df['close'].rolling(window=periodo).std()

    df['bb_upper'] = df['bb_middle'] + (2 * df['bb_std'])
    df['bb_lower'] = df['bb_middle'] - (2 * df['bb_std'])

    df.drop(['bb_std'], axis=1, inplace=True)
    return df


def calcular_stochastic(df, k_period=14, d_period=3):
    low_min = df['low'].rolling(window=k_period).min()
    high_max = df['high'].rolling(window=k_period).max()

    df['stochastic_k'] = 100 * (df['close'] - low_min) / (high_max - low_min)
    df['stochastic_d'] = df['stochastic_k'].rolling(window=d_period).mean()

    return df


def aplicar_indicadores(df):
    """
    Aplica todos os indicadores no dataframe.

    Args:
        df (DataFrame): Dados OHLCV

    Returns:
        DataFrame: Com indicadores adicionados
    """
    df = calcular_ema(df)
    df = calcular_rsi(df)
    df = calcular_macd(df)
    df = calcular_adx(df)
    df = calcular_bollinger_bands(df)
    df = calcular_stochastic(df)

    return df
    
