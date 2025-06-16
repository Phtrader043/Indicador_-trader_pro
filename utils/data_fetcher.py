import requests
import pandas as pd
from datetime import datetime
from utils import log, timezone_brasilia
from config import (
    CRYPTOCOMPARE_API_KEY,
    TWELVEDATA_API_KEY
)


# 🪙 Busca dados de criptomoedas pela CryptoCompare
def fetch_crypto_data(symbol, timeframe='5m', limit=100):
    """
    Busca dados históricos de criptomoedas.

    Args:
        symbol (str): Ex.: 'BTC/USDT'
        timeframe (str): Intervalo (ex.: '5m', '15m')
        limit (int): Número de velas

    Returns:
        DataFrame ou None
    """
    try:
        base, quote = symbol.split('/')
        url = f"https://min-api.cryptocompare.com/data/v2/histo{timeframe.replace('m', '')}"

        params = {
            'fsym': base,
            'tsym': quote,
            'limit': limit,
            'api_key': CRYPTOCOMPARE_API_KEY
        }

        response = requests.get(url, params=params)
        data = response.json()

        if data['Response'] != 'Success':
            log(f"[{symbol}] Erro na API CryptoCompare: {data.get('Message')}", "error")
            return None

        df = pd.DataFrame(data['Data']['Data'])
        df['time'] = pd.to_datetime(df['time'], unit='s')
        df = df.rename(columns={
            'time': 'datetime',
            'high': 'high',
            'low': 'low',
            'open': 'open',
            'close': 'close',
            'volumefrom': 'volume'
        })
        df.set_index('datetime', inplace=True)

        log(f"[{symbol}] Dados cripto coletados com sucesso.", "success")
        return df

    except Exception as e:
        log(f"[{symbol}] Erro ao coletar dados cripto: {e}", "error")
        return None


# 💱 Busca dados de Forex pela Twelve Data
def fetch_forex_data(symbol, timeframe='5min', limit=100):
    """
    Busca dados históricos de Forex.

    Args:
        symbol (str): Ex.: 'EUR/USD'
        timeframe (str): '1min', '5min', '15min'
        limit (int): Número de velas

    Returns:
        DataFrame ou None
    """
    try:
        symbol_td = symbol.replace('/', '')

        url = "https://api.twelvedata.com/time_series"

        params = {
            'symbol': symbol_td,
            'interval': timeframe,
            'outputsize': limit,
            'apikey': TWELVEDATA_API_KEY,
            'format': 'JSON'
        }

        response = requests.get(url, params=params)
        data = response.json()

        if 'values' not in data:
            log(f"[{symbol}] Erro na API Twelve Data: {data.get('message')}", "error")
            return None

        df = pd.DataFrame(data['values'])
        df['datetime'] = pd.to_datetime(df['datetime'])
        df = df.rename(columns={
            'open': 'open',
            'high': 'high',
            'low': 'low',
            'close': 'close',
            'volume': 'volume'
        })
        df[['open', 'high', 'low', 'close', 'volume']] = df[['open', 'high', 'low', 'close', 'volume']].astype(float)
        df.set_index('datetime', inplace=True)
        df = df.sort_index()

        log(f"[{symbol}] Dados Forex coletados com sucesso.", "success")
        return df

    except Exception as e:
        log(f"[{symbol}] Erro ao coletar dados Forex: {e}", "error")
        return None


# 🔍 Função única para escolher entre cripto ou forex
def fetch_data(asset, timeframe='5m', limit=100):
    """
    Busca dados dependendo se é Forex ou Cripto.

    Args:
        asset (str): 'BTC/USDT' ou 'EUR/USD'
        timeframe (str): Ex.: '5m'
        limit (int): Quantidade de velas

    Returns:
        DataFrame ou None
    """
    if '/' not in asset:
        log(f"Formato do ativo inválido: {asset}", "error")
        return None

    quote = asset.split('/')[1]

    # Define se é Forex ou Cripto (baseado no quote)
    forex_quotes = ['USD', 'EUR', 'GBP', 'JPY', 'AUD', 'NZD', 'CHF', 'CAD', 'SGD', 'NOK', 'SEK', 'DKK', 'PLN', 'TRY', 'ZAR', 'HKD']

    if quote in forex_quotes:
        return fetch_forex_data(asset, timeframe, limit)
    else:
        return fetch_crypto_data(asset, timeframe, limit)
