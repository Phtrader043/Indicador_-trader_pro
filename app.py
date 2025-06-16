import streamlit as st
from engine.signal_engine import gerar_sinal
from engine.trading_executor import executar_ordem_binance, executar_ordem_mt5
from config import MODO, TIMEFRAME

st.set_page_config(page_title="Indicador GPT 2.0", layout="wide", page_icon="📈")

st.image("assets/background.png", use_column_width=True)
st.title("📊 Indicador GPT 2.0 — Sinais Inteligentes Cripto & Forex")

st.sidebar.header("Configurações do Sinal")
ativo = st.sidebar.text_input("Ativo (Ex: BTCUSDT, EURUSD)", value="BTCUSDT")
plataforma = st.sidebar.selectbox("Plataforma", ["Binance", "MT5"])
quantidade = st.sidebar.number_input("Quantidade / Lote", value=0.01, step=0.001)
modo = st.sidebar.selectbox("Modo de Operação", ["Conservador", "Agressivo"], index=0)

st.sidebar.markdown("---")
if st.sidebar.button("🚀 Ativar IA e Gerar Sinal"):
    with st.spinner("Gerando sinal..."):
        resultado = gerar_sinal(ativo, TIMEFRAME, modo)

        if resultado:
            st.subheader("📑 Resultado do Sinal")
            st.json(resultado)

            if st.button("💰 Executar Ordem"):
                if plataforma == "Binance":
                    executar_ordem_binance(ativo, resultado['tipo'], quantidade)
                else:
                    executar_ordem_mt5(ativo, resultado['tipo'], quantidade)

                st.success("✔️ Ordem enviada com sucesso!")
        else:
            st.warning("⚠️ Nenhum sinal encontrado no momento.")