import pandas as pd
import numpy as np

# Ler o arquivo Excel
df = pd.read_excel('Banco de Cores.xlsx')

import cv2

# Carregar a imagem
imagem = cv2.imread('teste.jpg')

# Calcular a média de cor
media_cor = cv2.mean(imagem)

# A média de cor é retornada como (B, G, R, A).
# Portanto, vamos pegar apenas os três primeiros valores.
media_cor_rgb = media_cor[:3]

# Converter de BGR para RGB
media_cor_rgb = tuple(reversed(media_cor_rgb))
print("Média de cor (RGB invertido):", media_cor_rgb)

# Lista de cores RGB de referência
cores_referencia = [
    np.array(media_cor_rgb)
]

# Função para calcular a distância euclidiana entre duas cores RGB
def distancia_rgb(cor1, cor2):
    return np.sqrt(np.sum((cor1 - cor2) ** 2))

# Função para encontrar a cor mais próxima para uma entrada na tabela
def encontrar_cor_proxima(cor_referencia, cores_da_tabela, tolerancia=0):
    distancias = [distancia_rgb(cor_referencia, cor) for cor in cores_da_tabela]
    # Encontrar índices dentro da tolerância
    indices_dentro_da_tolerancia = [i for i, d in enumerate(distancias) if d <= tolerancia]
    # Se houver cores dentro da tolerância, retornar a mais próxima
    if indices_dentro_da_tolerancia:
        distancias_dentro_da_tolerancia = [distancias[i] for i in indices_dentro_da_tolerancia]
        indice_min_distancia = indices_dentro_da_tolerancia[np.argmin(distancias_dentro_da_tolerancia)]
        return cores_da_tabela[indice_min_distancia]
    # Caso contrário, retornar a mais próxima na lista completa
    else:
        indice_min_distancia = np.argmin(distancias)
        return cores_da_tabela[indice_min_distancia]

# Contador para contar as ocorrências de cada cor de referência como a mais próxima
contagem_cores_referencia = {tuple(cor): 0 for cor in cores_referencia}

# Encontrar a cor mais próxima para cada entrada na tabela
for index, linha in df.iterrows():
    cor_tabela = np.array([int(i) for i in linha['sRGB'].split(',')])
    cor_mais_proxima = encontrar_cor_proxima(cor_tabela, cores_referencia, tolerancia=10)  # Altere a tolerância conforme necessário
    contagem_cores_referencia[tuple(cor_mais_proxima)] += 1

# Determinar qual cor de referência foi escolhida como a mais próxima com mais frequência
cor_mais_frequente = max(contagem_cores_referencia, key=contagem_cores_referencia.get)

# Encontrar a cor mais próxima para cada cor de referência
for i, cor_referencia in enumerate(cores_referencia):
    cor_mais_proxima = encontrar_cor_proxima(cor_referencia, df['sRGB'].apply(lambda x: np.array([int(i) for i in x.split(',')])), tolerancia=10)  # Altere a tolerância conforme necessário
    print("Para a cor", i+1, "(", cor_referencia, "), a cor mais próxima é:", cor_mais_proxima)
