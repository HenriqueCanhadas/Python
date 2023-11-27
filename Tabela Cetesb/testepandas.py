import pandas as pd

# Leia o arquivo Excel e obtenha os valores da primeira coluna na guia "Table 2"
dados_excel = pd.read_excel('Tabela Cetesb/DD-125-2021-E-Atualizacao-dos-Valores-Orientadores-paa-solo-e-aguas-subterraneas.xlsx', sheet_name='Table 2', header=None)

# Lista de nomes que indicam o início da leitura
nomes_inicio_leitura = [
    "INORGÂNICOS",
    "HIDROCARBONETOS AROMÁTICOS VOLÁTEIS",
    "HIDROCARBONETOS POLICÍCLICOS AROMÁTICOS",
    "BENZENOS CLORADOS",
    "ETANOS CLORADOS",
    "ETENOS CLORADOS",
    "METANOS CLORADOS",
    "FENÓIS CLORADOS",
    "FENÓIS NÃO CLORADOS",
    "ÉSTERES FTÁLICOS",
    "PESTICIDAS",
    "OUTROS",
    "VRQ – Valor de Referência de Qualidade; VP – Valor de Prevenção; VI – Valor de Intervenção",
]

# Inicializar uma lista para armazenar os valores da coluna A
valores_coluna_a = []

# Variável para indicar se a leitura deve começar
comecar_leitura = False

# Iterar sobre os valores da coluna A
for valor in dados_excel.iloc[:, 0]:
    # Se o valor estiver na lista, comece a leitura
    if valor in nomes_inicio_leitura:
        comecar_leitura = True
    # Se a leitura já começou e o valor não está no final da lista e não é igual a nenhum item em nomes_inicio_leitura, adicione o valor à lista
    if comecar_leitura and valor != nomes_inicio_leitura[-1] and valor not in nomes_inicio_leitura:
        valores_coluna_a.append(valor)
    # Se o valor for igual a "VRQ – Valor de Referência de Qualidade; VP – Valor de Prevenção; VI – Valor de Intervenção", interrompa o loop
    if comecar_leitura and valor == nomes_inicio_leitura[-1]:
        break

# Crie um novo DataFrame com os valores da coluna A
novo_dataframe = pd.DataFrame({dados_excel.columns[0]: valores_coluna_a})

# Crie um novo arquivo Excel com base no novo DataFrame
novo_dataframe.to_excel('Tabela Cetesb/meuarquivo.xlsx', index=False)
