import streamlit as st
from signal_engine import gerar_sinal
from sentiment_analysis import analisar_sentimento_mercado
from utils import horario_brasilia, data_hora_brasilia, log
import pandas as pd


# =========================
# Configurações da Página
# =========================
st.set_page_config(
    page_title="Indicador GPT 2.0 - Cripto & Forex",
    page_icon="💹",
    layout="wide"
)

st.markdown(
    """
    <style>
        .stApp {
            background-color: #0f0f0f;
            background-image: url('https://images.unsplash.com/photo-1625566285125-6f7bdb6a8a3d');
            background-size: cover;
            color: white;
        }
    </style>
    """,
    unsafe_allow_html=True
)


# =========================
# Cabeçalho
# =========================
st.title("💹 Indicador GPT 2.0 - Cripto & Forex")

st.subheader(f"⏰ Horário de Brasília: {data_hora_brasilia()}")

st.markdown("---")


# =========================
# Sidebar
# =========================
st.sidebar.header("⚙️ Configurações")

modo = st.sidebar.radio(
    "Selecione o modo de operação:",
    ("Conservador", "Agressivo")
)

st.sidebar.markdown("---")

st.sidebar.subheader("🔮 Análise de Sentimento do Mercado")

if st.sidebar.button("🔍 Analisar Sentimento"):
    sentimento = analisar_sentimento_mercado()
    st.sidebar.success(f"Distribuição de Sentimento:\n\n{sentimento}")
    st.sidebar.write(sentimento)


st.sidebar.markdown("---")
st.sidebar.caption("Desenvolvido por Indicador GPT")


# =========================
# Corpo Principal
# =========================
st.subheader("📊 Geração de Sinais em Tempo Real")

col1, col2 = st.columns(2)

with col1:
    st.info("Clique no botão abaixo para ativar a IA e gerar sinais.")
    ativar = st.button("🚀 Ativar IA")

with col2:
    st.success(f"Modo selecionado: **{modo}**")


if ativar:
    with st.spinner("🔄 Gerando sinal..."):
        sinal = gerar_sinal(modo=modo)

        if sinal:
            df_sinal = pd.DataFrame([sinal])
            st.success("✅ Sinal Gerado com Sucesso!")
            st.table(df_sinal)

        else:
            st.warning("⚠️ Nenhum sinal gerado no momento. Aguarde e tente novamente.")

st.markdown("---")


# =========================
# Histórico de Sinais (Simulado)
# =========================
st.subheader("🕒 Histórico de Sinais Recentes")

historico = [
    {"Data": "16/06/2025", "Ativo": "BTC/USD", "Tendência": "Alta", "Entrada": 67000, "Saída": 67350, "Resultado": "✅"},
    {"Data": "16/06/2025", "Ativo": "EUR/USD", "Tendência": "Baixa", "Entrada": 1.0820, "Saída": 1.0785, "Resultado": "✅"},
    {"Data": "15/06/2025", "Ativo": "ETH/USD", "Tendência": "Alta", "Entrada": 3450, "Saída": 3480, "Resultado": "✅"},
    {"Data": "15/06/2025", "Ativo": "USD/JPY", "Tendência": "Baixa", "Entrada": 156.20, "Saída": 155.80, "Resultado": "❌"},
]

df_historico = pd.DataFrame(historico)
st.table(df_historico)

st.markdown("---")

# =========================
# Rodapé
# =========================
st.caption("📈 Desenvolvido por Indicador GPT 2.0 | IA + Análise Técnica + Sentimento de Mercado")
.warning("⚠️ Nenhum sinal encontrado no momento.")
