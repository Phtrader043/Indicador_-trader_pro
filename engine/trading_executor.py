from binance.client import Client
from utils import log
from config import BINANCE_API_KEY, BINANCE_API_SECRET


# 🔑 Conecta na Binance
client = Client(api_key=BINANCE_API_KEY, api_secret=BINANCE_API_SECRET)


def execute_trade(sinal):
    """
    Executa uma ordem na Binance baseada no sinal.

    Args:
        sinal (dict): Sinal gerado contendo:
                      - ativo
                      - sinal (COMPRA ou VENDA)
                      - entrada
                      - stop_loss
                      - take_profit
                      - modo
    """
    try:
        symbol = format_symbol(sinal['ativo'])
        side = 'BUY' if sinal['sinal'] == 'COMPRA' else 'SELL'
        quantidade = calculate_position_size(symbol, sinal['entrada'], sinal['modo'])

        if quantidade == 0:
            log(f"[{symbol}] Quantidade calculada é zero. Ordem cancelada.", "warning")
            return None

        # 🟩 Executa ordem a mercado
        order = client.create_order(
            symbol=symbol,
            side=side,
            type='MARKET',
            quantity=quantidade
        )

        log(f"[{symbol}] Ordem executada: {side} {quantidade}", "success")
        return order

    except Exception as e:
        log(f"[{sinal['ativo']}] Erro ao executar ordem: {e}", "error")
        return None


def format_symbol(ativo):
    """
    Formata o ativo para padrão da Binance.

    Ex.: BTC/USDT → BTCUSDT
    """
    return ativo.replace('/', '').upper()


def calculate_position_size(symbol, price, modo):
    """
    Calcula o tamanho da posição baseada no modo de risco.

    Args:
        symbol (str): Ativo
        price (float): Preço atual
        modo (str): 'Conservador' ou 'Agressivo'

    Returns:
        float: Quantidade
    """
    # 🧠 Exemplos de gestão — você pode personalizar aqui:
    saldo = get_balance('USDT')

    risco = 0.01 if modo == "Conservador" else 0.03
    valor_risco = saldo * risco

    quantidade = valor_risco / price

    # Verifica lotes mínimos da Binance
    quantidade = round_quantity(symbol, quantidade)

    return quantidade


def get_balance(asset):
    """
    Retorna saldo disponível
