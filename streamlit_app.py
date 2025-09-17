import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from pathlib import Path

# -------------------------------
# Configuração básica da página
# -------------------------------
st.set_page_config(page_title="Sense — Dashboard", layout="wide")
st.title("📊 Sense — RFM, Clusters, Tendência & Testes de Hipótese")

OUT_DIR = Path("Output")

# -------------------------------
# Helper simples (ok manter)
# -------------------------------
def load_csv(name: str):
    path = OUT_DIR / name
    return pd.read_csv(path) if path.exists() else None

# -------------------------------
# Carregamento de dados
# -------------------------------
rfm_with_clusters = load_csv("rfm_with_clusters.csv")
cluster_profiles   = load_csv("cluster_profiles.csv")
monthly_trend      = load_csv("monthly_events_trend.csv")
anova_results      = load_csv("anova_results.csv")
tukey_results      = load_csv("tukey_results.csv")
predictions        = load_csv("predictions_m_plus_1.csv")
exec_summary       = load_csv("executive_summary.csv")

# -------------------------------
# Sidebar: status dos arquivos
# -------------------------------
st.sidebar.header("Arquivos carregados")
for fname in [
    "rfm_with_clusters.csv",
    "cluster_profiles.csv",
    "monthly_events_trend.csv",
    "anova_results.csv",
    "tukey_results.csv",
    "predictions_m_plus_1.csv",
    "executive_summary.csv",
]:
    exists = (OUT_DIR / fname).exists()
    st.sidebar.write(f"- {fname} {'✅' if exists else '❌'}")

# -------------------------------
# Abas
# -------------------------------
tab1, tab2, tab3 = st.tabs(["Clusters (RFM)", "Tendência mensal", "Testes de hipótese"])

# -------------------------------
# Aba 1: Clusters (RFM)
# -------------------------------
with tab1:
    st.subheader("RFM com Clusters")
    if rfm_with_clusters is not None and not rfm_with_clusters.empty:
        st.dataframe(rfm_with_clusters.head(50))

        if 'cluster' in rfm_with_clusters.columns and 'monetary' in rfm_with_clusters.columns:
            means = rfm_with_clusters.groupby('cluster')['monetary'].mean().sort_values()
            fig, ax = plt.subplots(figsize=(6, 4))
            means.plot(kind='bar', ax=ax)
            ax.set_title("Média de Monetary por Cluster")
            ax.set_xlabel("Cluster")
            ax.set_ylabel("Monetary (média)")
            st.pyplot(fig)
    else:
        st.info("rfm_with_clusters.csv não encontrado.")

    st.subheader("Perfis de Cluster")
    if cluster_profiles is not None and not cluster_profiles.empty:
        st.dataframe(cluster_profiles)
    else:
        st.info("cluster_profiles.csv não encontrado.")

# -------------------------------
# Aba 2: Tendência mensal
# -------------------------------
with tab2:
    st.subheader("Tendência Mensal de Eventos")
    if monthly_trend is not None and not monthly_trend.empty:
        # Normaliza coluna de data
        cols = [c.lower() for c in monthly_trend.columns]
        monthly_trend.columns = cols

        # Detecta coluna de mês/data
        month_col = None
        for c in monthly_trend.columns:
            if any(k in c for k in ['month', 'mes', 'data', 'date', 'dt', 'period']):
                month_col = c
                break

        # Detecta coluna numérica principal (events)
        events_col = 'events' if 'events' in monthly_trend.columns else None
        if events_col is None:
            num_cols = [c for c in monthly_trend.columns if pd.api.types.is_numeric_dtype(monthly_trend[c])]
            num_cols = [c for c in num_cols if c != month_col]
            events_col = num_cols[0] if num_cols else None

        if month_col is not None and events_col is not None:
            monthly_trend[month_col] = pd.to_datetime(monthly_trend[month_col], errors='coerce')
            monthly_trend = monthly_trend.dropna(subset=[month_col]).sort_values(month_col)

            fig2, ax2 = plt.subplots(figsize=(8, 4))
            ax2.plot(monthly_trend[month_col], monthly_trend[events_col], label=events_col)
            if 'ma' in monthly_trend.columns:
                ax2.plot(monthly_trend[month_col], monthly_trend['ma'], label='moving avg (6m)')
            ax2.set_title("Eventos por mês")
            ax2.set_xlabel("Mês")
            ax2.set_ylabel("Eventos")
            ax2.legend()
            st.pyplot(fig2)

            if predictions is not None and not predictions.empty:
                st.markdown("**Previsão M+1 (eventos):**")
                st.dataframe(predictions)
        else:
            st.warning("Não foi possível identificar colunas de mês e eventos no CSV.")
    else:
        st.info("monthly_events_trend.csv não encontrado.")

# -------------------------------
# Aba 3: Testes de hipótese
# -------------------------------
with tab3:
    st.subheader("ANOVA")
    if anova_results is not None and not anova_results.empty:
        st.dataframe(anova_results)
        if 'p_value' in anova_results.columns:
            try:
                pv = float(anova_results['p_value'].min())
                st.write(f"**Menor p-value:** {pv:.6f} — valores < 0.05 sugerem diferença significativa de médias entre grupos.")
            except Exception:
                pass
    else:
        st.info("anova_results.csv não encontrado.")

    st.subheader("Tukey HSD (pares de clusters)")
    if tukey_results is not None and not tukey_results.empty:
        st.dataframe(tukey_results)
        st.caption("Coluna 'reject' = True indica pares com diferença significativa (α=0.05).")
    else:
        st.info("tukey_results.csv não encontrado.")

# -------------------------------
# Rodapé/Sidebar
# -------------------------------
st.sidebar.markdown("---")
st.sidebar.write("Dica: gere os CSVs rodando o notebook primeiro.")
