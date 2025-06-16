import cohere
from config import COHERE_API_KEY
from utils import log


# 🔑 Conecta na API da Cohere
co = cohere.Client(COHERE_API_KEY)


def validar_sinal_com_ia(sinal):
    """
    Valida o sinal utilizando IA da Cohere.

    Args:
        sinal (dict): Dados do sinal com:
            - ativo
            - sinal (COMPRA ou VENDA)
            - tendência
            - indicadores (RSI, MACD, etc.)

    Returns:
        bool: True se a IA confirmar o sinal, False se rejeitar
    """

    prompt = gerar_prompt(sinal)

    try:
        resposta = co.generate(
            model='command-r',
            prompt=prompt,
            max_tokens=100,
            temperature=0.2
        )

        texto = resposta.generations[0].text.strip().lower()

        log(f"Resposta IA: {texto}")

        if "aceito" in texto or "confirmo" in texto or "válido" in texto:
            return True
        else:
            return False

    except Exception as e:
        log(f"Erro na análise Cohere: {e}", "error")
        return False


def gerar_prompt(sinal):
    """
    Gera o prompt de validação para a IA da Cohere.

    Args:
        sinal (dict): Dados do sinal

    Returns:
        str: Texto do prompt
    """
    prompt = f"""
Você é um assistente especialista em trading e mercados financeiros.

Analise o seguinte sinal e me diga se ele é um sinal confiável para executar uma operação no mercado.

Dados do sinal:
- Ativo: {sinal['ativo']}
- Tipo: {sinal['sinal']}
- Tendência: {sinal['tendencia']}%
- Indicadores Técnicos:
  • RSI: {sinal.get('rsi')}
  • MACD: {sinal.get('macd')}
  • EMA: {sinal.get('ema')}
  • ADX: {sinal.get('adx')}
  • Bandas de Bollinger: {sinal.get('bollinger')}
  • Estocástico: {sinal.get('stochastic')}

Baseado nesses dados, este sinal é confiável para abrir uma operação?

Responda de forma direta apenas com uma das opções:
- Aceito, é um sinal confiável.
- Recusado, não é um sinal confiável.

Explique em poucas palavras se desejar.
"""
    return prompt
