import requests
import pandas as pd
from cohere import Client
from config import COHERE_API_KEY
from utils import log


# Inicializa a API da Cohere
cohere = Client(COHERE_API_KEY)


def analisar_sentimento_texto(texto):
    """
    Faz a análise de sentimento de um texto usando IA (Cohere).

    Args:
        texto (str): Texto a ser analisado.

    Returns:
        str: 'Positivo', 'Neutro' ou 'Negativo'
    """
    try:
        prompt = f"""
        Classifique o sentimento do seguinte texto relacionado ao mercado financeiro e criptomoedas como Positivo, Neutro ou Negativo:
        Texto: "{texto}"
        Resposta:
        """

        response = cohere.generate(
            model='command',
            prompt=prompt,
            max_tokens=10,
            temperature=0.3,
        )

        sentimento = response.generations[0].text.strip().lower()

        if "positivo" in sentimento:
            return "Positivo"
        elif "negativo" in sentimento:
            return "Negativo"
        else:
            return "Neutro"

    except Exception as e:
        log(f"Erro na análise de sentimento: {e}", "error")
        return "Neutro"


def coletar_noticias_binance_feed():
    """
    Simula coleta de notícias do feed da Binance (ou substituto via API pública, RSS, etc).

    Returns:
        lista: Lista de manchetes recentes
    """
    try:
        # 🔥 Simulação de dados - você pode integrar com uma API real como:
        # - Crypto Panic API
        # - News API
        # - RSS Feeds

        noticias = [
            "Bitcoin dispara após dados de inflação nos EUA",
            "Ethereum apresenta instabilidade após atualização",
            "Mercado cripto reage negativamente à decisão do FED",
            "SEC abre investigação sobre corretora cripto",
            "Alta adoção do Bitcoin na América Latina impulsiona mercado"
        ]

        return noticias

    except Exception as e:
        log(f"Erro ao coletar notícias: {e}", "error")
        return []


def analisar_sentimento_mercado():
    """
    Faz análise de sentimento geral do mercado baseado em manchetes.

    Returns:
        dict: Resultado da análise com distribuição dos sentimentos
    """
    noticias = coletar_noticias_binance_feed()
    resultados = []

    for noticia in noticias:
        sentimento = analisar_sentimento_texto(noticia)
        resultados.append(sentimento)

    df = pd.DataFrame(resultados, columns=["sentimento"])
    distribuicao = df['sentimento'].value_counts().to_dict()

    # Calcula o percentual de cada sentimento
    total = sum(distribuicao.values())
    distribuicao_percentual = {k: round((v / total) * 100, 2) for k, v in distribuicao.items()}

    log(f"Distribuição de sentimento do mercado: {distribuicao_percentual}", "info")

    return distribuicao_percentual


def sentimento_para_sinal(distribuicao):
    """
    Converte análise de sentimento para tendência de mercado.

    Args:
        distribuicao (dict): Saída de analisar_sentimento_mercado()

    Returns:
        str: 'Alta', 'Baixa' ou 'Neutro'
    """
    positivo = distribuicao.get('Positivo', 0)
    negativo = distribuicao.get('Negativo', 0)

    if positivo > negativo + 20:
        return "Alta"
    elif negativo > positivo + 20:
        return "Baixa"
    else:
        return "Neutro"
