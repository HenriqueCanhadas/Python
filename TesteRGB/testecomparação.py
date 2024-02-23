import pandas as pd
import numpy as np

# Ler o arquivo Excel
df = pd.read_excel('Banco de Cores.xlsx')


# Lista de cores RGB de referência
cores_referencia = [
    np.array([195, 152, 86]),
    np.array([129, 110, 89]),
    np.array([62, 46, 30]),
    np.array([192, 170, 146]),
    np.array([96, 79, 61])
]

# Função para calcular a distância euclidiana entre duas cores RGB
def distancia_rgb(cor1, cor2):
    return np.sqrt(np.sum((cor1 - cor2) ** 2))

# Função para encontrar a cor mais próxima para uma entrada na tabela
def encontrar_cor_proxima(cor_referencia, cores_da_tabela):
    distancias = [distancia_rgb(cor_referencia, cor) for cor in cores_da_tabela]
    indice_min_distancia = np.argmin(distancias)
    return cores_da_tabela[indice_min_distancia]

# Contador para contar as ocorrências de cada cor de referência como a mais próxima
contagem_cores_referencia = {tuple(cor): 0 for cor in cores_referencia}

# Encontrar a cor mais próxima para cada entrada na tabela
for index, linha in df.iterrows():
    cor_tabela = np.array([int(i) for i in linha['sRGB'].split(',')])
    cor_mais_proxima = encontrar_cor_proxima(cor_tabela, cores_referencia)
    contagem_cores_referencia[tuple(cor_mais_proxima)] += 1

# Determinar qual cor de referência foi escolhida como a mais próxima com mais frequência
cor_mais_frequente = max(contagem_cores_referencia, key=contagem_cores_referencia.get)

print("A cor de referência mais frequentemente escolhida como a mais próxima é:", cor_mais_frequente)
# Encontrar a cor mais próxima para cada cor de referência
for i, cor_referencia in enumerate(cores_referencia):
    cor_mais_proxima = encontrar_cor_proxima(cor_referencia, df['sRGB'].apply(lambda x: np.array([int(i) for i in x.split(',')])))
    print("Para a cor", i+1, "(", cor_referencia, "), a cor mais próxima é:", cor_mais_proxima)