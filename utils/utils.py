from datetime import datetime
import pytz

def horario_brasilia():
    tz = pytz.timezone("America/Sao_Paulo")
    return datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")

def normalizar_nome_ativo(ativo):
    return ativo.replace("/", "")