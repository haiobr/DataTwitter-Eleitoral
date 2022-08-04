import pandas as pd
import streamlit as st
from PIL import Image


st.title('Jornada Além dos Dados')
st.text('Aplicação que realiza análise de sentimento dos candidatos à presidência usando dados do Twitter')


df = pd.read_csv('dataframe_final.csv')

candidato_unico = sorted(df['Candidato'].unique())
selecionar_candidato = st.sidebar.multiselect('Candidato', candidato_unico, candidato_unico)

df_candidato_selecionado = df[(df['Candidato'].isin(selecionar_candidato))]
st.write('Conjunto de Dados ' + str(df_candidato_selecionado.shape[0]) + ' linhas')  ##+ str(df_candidato_selecionado.len[0]))


st.dataframe(df_candidato_selecionado)


