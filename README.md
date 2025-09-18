---

# FIAP Sprint Final — Sense

**Resumo do projeto**

Pipeline simples (nível acadêmico) para **segmentação de clientes** via RFM +  **KMeans** , **previsão M+1** (modelos básicos como Regressão Linear e baseline ingênuo) e **testes de hipótese** (ANOVA + Tukey) para validar diferenças entre clusters. Exporta **CSVs** e **gráficos** prontos para BI. [GitHub](https://github.com/helgg/fiap-sprint-final-sense/tree/master)

## Bibliotecas principais

* pandas, numpy
* scikit-learn (KMeans, LinearRegression)
* scipy (ANOVA)
* statsmodels (Tukey HSD)
* matplotlib (gráficos)

## Instalação (requirements)

Crie um ambiente virtual e instale as dependências do projeto:

```
# Clonar o repo
git clone https://github.com/helgg/fiap-sprint-final-sense.git
cd fiap-sprint-final-sense

# (Linux/Mac)
python -m venv .venv
source .venv/bin/activate

# (Windows PowerShell)
# python -m venv .venv
# .venv\Scripts\Activate.ps1

# Atualizar pip e instalar requirements
python -m pip install -U pip
pip install -r requirements.txt
```

## Objetivos

- **Segmentação** de clientes via **RFM** (Recência, Frequência, Monetário) + **KMeans**.
- **Previsão M+1** (ex.: receita ou frequência no próximo mês) usando modelos simples e explicáveis.
- **Detecção de anomalias** para identificar clientes/compras fora do padrão.
- **Validação estatística** das diferenças entre segmentos (ANOVA + pós-teste **Tukey HSD**).
- **Exportação** de resultados em **CSV** e geração de **gráficos** para dashboards.
