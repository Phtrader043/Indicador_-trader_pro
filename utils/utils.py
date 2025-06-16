import pytz
from datetime import datetime
import time
import logging


# =========================
# Configuração de Logs
# =========================
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler("logs.txt"),
        logging.StreamHandler()
    ]
)


def log(mensagem, tipo="info"):
    """
    Função de log padronizada.
    Args:
        mensagem (str): Mensagem a ser exibida
        tipo (str): 'info', 'warning', 'error'
    """
    if tipo == "info":
        logging.info(mensagem)
    elif tipo == "warning":
        logging.warning(mensagem)
    elif tipo == "error":
        logging.error(mensagem)
    else:
        logging.info(mensagem)


# =========================
# Horário de Brasília
# =========================
def horario_brasilia():
    """
    Retorna o horário atual de Brasília formatado.
    Returns:
        str: Hora atual no formato HH:MM:SS
    """
    fuso_brasilia = pytz.timezone('America/Sao_Paulo')
    agora = datetime.now(fuso_brasilia)
    return agora.strftime('%H:%M:%S')


def data_hora_brasilia():
    """
    Retorna a data e hora atual de Brasília.
    Returns:
        str: Data e hora no formato DD/MM/YYYY HH:MM:SS
    """
    fuso_brasilia = pytz.timezone('America/Sao_Paulo')
    agora = datetime.now(fuso_brasilia)
    return agora.strftime('%d/%m/%Y %H:%M:%S')


# =========================
# Controle de Erros 429
# =========================
def aguardar_requisicao(segundos=60):
    """
    Aguarda determinado tempo antes de fazer uma nova requisição.
    Útil para tratar erros 429 (limite de requisições).
    Args:
        segundos (int): Tempo em segundos para aguardar.
    """
    log(f"Aguardando {segundos} segundos para evitar limite de requisições...", "warning")
    time.sleep(segundos)


# =========================
# Funções de Utilidade Geral
# =========================
def formatar_ativo(ativo):
    """
    Formata o nome do ativo para exibição.
    Args:
        ativo (str): Código do ativo (ex.: BTC/USD)
    Returns:
        str: Ativo formatado
    """
    return ativo.replace("/", " / ")


def checar_nan_ou_invalido(valor):
    """
    Verifica se um valor é NaN, None ou inválido.
    Args:
        valor: Valor a ser checado
    Returns:
        bool: True se inválido, False se válido
    """
    return valor is None or valor != valor


def validar_dataframe(df):
    """
    Verifica se o dataframe possui dados válidos.
    Args:
        df (DataFrame): DataFrame a ser validado
    Returns:
        bool: True se válido, False se vazio ou inválido
    """
    if df is None:
        return False
    if df.empty:
        return False
    if df.isnull().values.all():
        return False
    return True
