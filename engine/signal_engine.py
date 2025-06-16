import pandas as pd
from indicators import calculate_indicators
from cohere_analysis import validate_with_ai
from risk_management import apply_risk_management
from utils import log, timezone_brasilia


def generate_trade_signal(df, asset, mode="Conservador"):
    """
    Gera sinais de trade baseado em indicadores técnicos e IA.

    Args:
        df (DataFrame): Dados de OHLCV.
        asset (str): Nome do ativo.
        mode (str): 'Conservador' ou 'Agressivo'.

    Returns:
        dict ou None: Sinal gerado ou None se não houver sinal.
    """
    try:
        if df is None or df.empty:
            log(f"[{asset}] Dados insuficientes para análise.", "warning")
            return None

        # 1️⃣ Calcula indicadores técnicos
        df_ind = calculate_indicators(df)

        # 2️⃣ Avalia condições de entrada
        last = df_ind.iloc[-1]

        rsi = last['RSI']
        macd = last['MACD']
        signal_macd = last['MACD_signal']
        adx = last['ADX']
        ema_fast = last['EMA_fast']
        ema_slow = last['EMA_slow']
        close = last['close']

        # Critérios técnicos básicos
        tendencia_alta = ema_fast > ema_slow and macd > signal_macd and adx > 20
        tendencia_baixa = ema_fast < ema_slow and macd < signal_macd and adx > 20

        sobrecomprado = rsi > 70
        sobrevendido = rsi < 30

        sinal = None

        if tendencia_alta and not sobrecomprado:
            sinal = "COMPRA"
        elif tendencia_baixa and not sobrevendido:
            sinal = "VENDA"

        if not sinal:
            log(f"[{asset}] Nenhum sinal técnico identificado.", "info")
            return None

        # 3️⃣ Validação com IA da Cohere
        validado = validate_with_ai(asset, sinal, df_ind)

        if not validado:
            log(f"[{asset}] Sinal técnico [{sinal}] REPROVADO pe
