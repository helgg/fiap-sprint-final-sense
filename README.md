
# fiap-sprint-final-sense

**RFM + KMeans** para segmentar clientes, **previsão M+1** e **detecção de anomalias**, com **testes de hipótese (ANOVA/Tukey)**.Gera **relatórios CSV** e **gráficos** prontos para análise em BI.

> Repositório: helgg/fiap-sprint-final-sense

---

## ✨ Objetivos

- **Segmentação** de clientes via **RFM** (Recência, Frequência, Monetário) + **KMeans**.
- **Previsão M+1** (ex.: receita ou frequência no próximo mês) usando modelos simples e explicáveis.
- **Detecção de anomalias** para identificar clientes/compras fora do padrão.
- **Validação estatística** das diferenças entre segmentos (ANOVA + pós-teste **Tukey HSD**).
- **Exportação** de resultados em **CSV** e geração de **gráficos** para dashboards.

---

## 🗂️ Estrutura (proposta)

```
.
├─ README.md
├─ script.ipynb        # Notebook principal com todo o pipeline
└─ output/             # (gerado pelo notebook) CSVs e gráficos
   ├─ rfm_segments.csv
   ├─ predictions_m_plus_1.csv
   ├─ anomalies.csv
   └─ charts/
```

> Observação: a pasta `output/` é criada pelo notebook (ou crie manualmente).

---

## 🔧 Stack (mínima)

- Python 3.10+
- Bibliotecas: `pandas`, `numpy`, `scikit-learn`, `scipy`, `matplotlib`, `statsmodels` (para Tukey)

Instalação rápida:

```
python -m venv .venv
source .venv/bin/activate   # no Windows: .venv\Scripts\activate
pip install -U pip
pip install pandas numpy scikit-learn scipy matplotlib statsmodels
```

---

## ▶️ Como executar

1. **Clone** o repositório:
   ```
   git clone https://github.com/helgg/fiap-sprint-final-sense.git
   cd fiap-sprint-final-sense
   ```
2. **Crie o ambiente** e **instale dependências** (comandos acima).
3. **Abra o notebook**:
   ```
   jupyter notebook script.ipynb
   ```
4. **Execute as células** de cima para baixo.
   - Parâmetros (ex.: caminhos de entrada/saída, `random_state`, número de clusters) ficam no topo do notebook.
5. Ao final, os **CSVs** e **gráficos** serão salvos em `output/`.

---

## 🔬 Pipeline (etapas do notebook)

1. **Ingestão e preparo**: leitura, limpeza básica e ajustes de tipos.
2. **Feature engineering (RFM)**: cálculo de Recência, Frequência e Monetário por cliente.
3. **Padronização** das features (quando necessário).
4. **KMeans**
   - Escolha de **k** (método do cotovelo e/ou silhouette).
   - Treinamento e atribuição de **segmentos** (clusters).
5. **Previsão M+1**
   - Modelos simples (ex.: regressão) para prever próxima janela (M+1).
   - Avaliação com métricas intuitivas (ex.: RMSE, R²).
6. **Anomalias**
   - Abordagem simples e transparente (ex.: **IQR** ou **Z-score**; opcional: IsolationForest).
7. **Testes de hipótese**
   - **ANOVA** para comparar médias entre clusters.
   - **Tukey HSD** para identificar quais pares diferem.
8. **Exportação**
   - **CSVs** com segmentos, previsões e anomalias.
   - **Gráficos** (ex.: cotovelo, distribuição R/F/M por cluster, barras comparativas).

---

## 📦 Saídas esperadas

- `output/rfm_segments.csv` — cliente, R, F, M, **cluster** e estatísticas de grupo.
- `output/predictions_m_plus_1.csv` — alvo real vs. previsto para M+1, erros e métricas.
- `output/anomalies.csv` — registros sinalizados como outliers + score/regra.
- `output/charts/` — imagens (PNG) dos principais gráficos usados no relatório.

> Os nomes podem variar conforme sua implementação; ajuste no notebook conforme necessário.

---

## 📊 Interpretação (exemplo)

- **Clusters RFM**: perfis como *VIP* (alto M e F, baixa R), *recém-ativos*, *inativos*, etc.
- **ANOVA/Tukey**: confirma se diferenças (ex.: ticket médio) entre clusters são **estatisticamente significativas**.
- **M+1**: prioriza **simplicidade e explicabilidade** nas previsões (útil para apresentar em sala/BI).
- **Anomalias**: alerta sobre comportamentos extremos (fraude/erros/dados raros).

---

## 🧪 Reprodutibilidade

- Defina `RANDOM_STATE` (ex.: `42`) no topo do notebook para resultados consistentes.
- Documente a versão das libs com:
  ```
  python -c "import pkgutil,sys; print(sys.version); print('\\n'.join(sorted([m.name for m in pkgutil.iter_modules()])))"
  ```

---

## ✅ Boas práticas adotadas

- Código **simples**, com **comentários** e métricas claras (nível universitário).
- **Exportação em CSV** para fácil integração em **Power BI**, **Looker Studio** etc.
- **Gráficos** salvos em arquivo, prontos para apresentação.

---

## 📌 Próximos passos (sugestões)

- Matriz de **confusão** (quando o alvo for classe) ou **curva de resíduos** (regressão).
- **SHAP**/**Permutation Importance** para interpretabilidade avançada (opcional).
- **Validação temporal** para M+1 (split por data).
- Pipeline em **Streamlit** para demo interativa (opcional).

---

## 📄 Licença

Defina a licença do projeto (ex.: MIT). Se não tiver, crie um `LICENSE`.

---

## ✍️ Autor

**Helder Gualdi de Godoy (helgg)** — Data Engineer & FIAP DS.
Repositório público: helgg/fiap-sprint-final-sense
