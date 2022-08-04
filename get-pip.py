import pandas as pd
import streamlit as st
from PIL import Image

# Título
st.title('Jornada Além dos Dados')
# Sub-título
st.text('Aplicação que realiza análise de sentimento dos candidatos à presidência usando dados do Twitter')

# Leitura do dataset
df = pd.read_csv('dataframe_final.csv')

# Ordenar valores únicos
candidato_unico = sorted(df['Candidato'].unique())
# Criar caixa de seleção com os nomes dos candidatos
selecionar_candidato = st.sidebar.multiselect('Candidato', candidato_unico, candidato_unico)
df_candidato_selecionado = df[(df['Candidato'].isin(selecionar_candidato))]

# Título informativo - Dataset
st.write('Conjunto de Dados possui ' + str(df_candidato_selecionado.shape[0]) + ' linhas')  ##+ str(df_candidato_selecionado.len[0]))

## Visualizar dataset
st.dataframe(df_candidato_selecionado)


