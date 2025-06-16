
# =========================
# 🔐 Configurações de API
# =========================
NEWS_API_KEY = "7686cc5d35ef4881906b682e80a45af8"

# API CryptoCompare (para Criptomoedas)
CRYPTOCOMPARE_API_KEY = "acc8c5e745f48879ac2770b2009c448f369a12b01bebae5161238c33f26a4092"

# API TwelveData (para Forex)
TWELVEDATA_API_KEY = "018d50c59fd94ddd8cf8a771c2bb5065"

# API Cohere (Análise de Linguagem e IA)
COHERE_API_KEY = "vVxHSphSMlg9MD43GlOstg8ZknQAZSt2lTdJ8gzC"

# API Binance (para execução de ordens reais em Cripto)
BINANCE_API_KEY = "gIEqsiEnDzTBJFR8fopgdSGAnvR2H6gWAdEmFVyF4nmBgoBSgn0FY7uodK2plz9U"
BINANCE_API_SECRET = "2KCewTDJhwW0e0x3S5I8VfVIz67C9sDH6eRh6gqQNpubHZrWd6qAhCSqKFnjaI2v"

# MT5 (para execução de ordens reais em Forex)
MT5_LOGIN = 123456
MT5_PASSWORD = "SUA_SENHA_MT5"
MT5_SERVER = "NOME_DO_SERVIDOR_MT5"


# =========================
# ⚙️ Configurações Globais
# =========================

# Lista de Criptomoedas a serem analisadas
CRIPTO_ATIVOS = [
    "BTC/USD", "ETH/USD", "BNB/USD", "SOL/USD", "ADA/USD",
    "XRP/USD", "DOT/USD", "LTC/USD", "DOGE/USD", "AVAX/USD"
]

# Lista completa de Pares Forex
FOREX_ATIVOS = [
    "EUR/USD", "USD/JPY", "GBP/USD", "USD/CHF", "AUD/USD", "USD/CAD", "NZD/USD",
    "EUR/GBP", "EUR/JPY", "EUR/CHF", "GBP/JPY", "GBP/CHF", "AUD/JPY", "AUD/NZD",
    "CAD/JPY", "CHF/JPY", "EUR/AUD", "EUR/CAD", "EUR/NZD", "GBP/AUD", "GBP/CAD",
    "GBP/NZD", "AUD/CAD", "AUD/CHF", "CAD/CHF", "NZD/JPY", "NZD/CAD", "NZD/CHF",
    "USD/SGD", "SGD/JPY", "USD/HKD", "USD/NOK", "USD/SEK", "USD/DKK", "USD/PLN",
    "USD/TRY", "USD/ZAR", "EUR/SEK", "EUR/NOK", "EUR/PLN", "EUR/TRY", "EUR/ZAR",
    "GBP/SEK", "GBP/NOK", "GBP/PLN", "AUD/SGD", "NZD/SGD", "SGD/CHF", "CHF/SEK",
    "NOK/JPY"
]


# =========================
# 🎯 Parâmetros de Trading
# =========================

# Modo padrão
MODO_OPERACAO = "Conservador"  # ou "Agressivo"

# Timeframe da análise
TIMEFRAME = "5min"

# Tolerância de spread em Forex
SPREAD_MAXIMO = 1.5  # percentual

# Delay entre checagens automáticas (em segundos)
DELAY_CHECAGEM = 60


# =========================
# 🛑 Gestão de Risco
# =========================

# Percentual máximo de risco por operação
RISCO_POR_OPERACAO = 1.5  # 1.5%

# Meta diária de lucro (%)
META_DIARIA = 5.0

# Limite de perda diária (%)
LIMITE_PERDA_DIARIA = 3.0

# Stop móvel ativado
USAR_STOP_MOVEL = True

# Break-even ativado
USAR_BREAK_EVEN = True

# Take Profit fixo (opcional, em %)
TAKE_PROFIT_FIXO = 2.5

# Stop Loss fixo (opcional, em %)
STOP_LOSS_FIXO = 1.5


# =========================
# 🔊 Alertas e Logs
# =========================

ATIVAR_ALERTA_SONORO = True
ATIVAR_LOGS = True


# =========================
# ⏰ Horário e Tempo
# =========================

# Fuso horário padrão
TIMEZONE = 'America/Sao_Paulo'

# Aguardar em caso de erro 429 (em segundos)
TEMPO_ESPERA_ERRO_429 = 60
