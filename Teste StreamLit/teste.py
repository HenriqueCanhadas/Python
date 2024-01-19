import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Definindo o título da aba, ícone e layout
titulo_aba = "Meu Aplicativo"
icone_aba = "👀"  # Substitua pelo emoji ou caminho do ícone desejado
layout_aba = "centered"  # Outras opções: "centered"

# Usando st.set_page_config para configurar título, ícone e layout da aba
st.set_page_config(page_title=titulo_aba, page_icon=icone_aba, layout=layout_aba)

# Define o estilo Seaborn
sns.set_style("darkgrid")  # Substitua "darkgrid" pelo estilo desejado

# Título do aplicativo
st.title('Aplicativo Streamlit Interativo')

# Sidebar para configurações
st.sidebar.header('Configurações')

# Número de pontos
num_pontos = st.sidebar.slider('Número de Pontos:', min_value=1, max_value=200, value=90)

# Tipo de gráfico
tipo_grafico = st.sidebar.selectbox('Selecione o Tipo de Gráfico:', ['Scatter Plot', 'Line Plot', 'Box Plot'])

# Criando um dataframe de exemplo
dados = pd.DataFrame({
    'x': np.random.randint(0, 101, size=num_pontos),
    'y': np.random.randint(0, 101, size=num_pontos)
})

# Adicionando um gráfico interativo com base na escolha do usuário
fig, ax = plt.subplots()

if tipo_grafico == 'Scatter Plot':
    scatter = ax.scatter(dados['x'], dados['y'])
elif tipo_grafico == 'Line Plot':
    line = ax.plot(dados['x'], dados['y'], marker='o')
elif tipo_grafico == 'Box Plot':
    boxplot = sns.boxplot(x=dados['x'], y=dados['y'])

# Adicionando título ao gráfico
ax.set_title(f'{tipo_grafico} - Número de Pontos: {num_pontos}')

# Definindo intervalos fixos nos eixos x e y
ax.set_xticks(np.arange(0, 101, 10))
ax.set_yticks(np.arange(0, 101, 10))

# Adicionando a figura ao Streamlit
st.pyplot(fig)

# Adicionando uma seção para personalizar o estilo do gráfico
st.header('Personalizar Estilo do Gráfico')

# Cor do fundo
cor_fundo = st.color_picker('Selecione a Cor do Fundo do Gráfico', '#FFFFFF')

# Cor da linha ou pontos
cor_linha_pontos = st.color_picker('Selecione a Cor da Linha ou Pontos', '#1f77b4')

# Atualizando o estilo do gráfico com base nas escolhas do usuário
fig, ax = plt.subplots()

if tipo_grafico == 'Scatter Plot':
    scatter = ax.scatter(dados['x'], dados['y'], c=cor_linha_pontos)
elif tipo_grafico == 'Line Plot':
    line = ax.plot(dados['x'], dados['y'], marker='o', color=cor_linha_pontos)
elif tipo_grafico == 'Box Plot':
    boxplot = sns.boxplot(x=dados['x'], y=dados['y'], color=cor_linha_pontos)

# Personalizando o estilo do gráfico
ax.set_facecolor(cor_fundo)
ax.set_title(f'{tipo_grafico} - Número de Pontos: {num_pontos}', color=cor_linha_pontos)

# Adicionando a figura ao Streamlit
st.pyplot(fig)
