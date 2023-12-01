import pandas as pd

# Leia os nomes de todas as abas
arquivo_excel = pd.ExcelFile('Tabela Epa/Dados_Tabelados_com_Abas.xlsx')
nomes_abas = arquivo_excel.sheet_names

# Lista para armazenar os DataFrames de cada aba
abas = []

# Itere sobre os nomes das abas e leia os dados
for i, nome_aba in enumerate(nomes_abas):
    aba = pd.read_excel(arquivo_excel, sheet_name=nome_aba)

    if i == 0:
        # Para a primeira aba, pegue todas as colunas
        abas.append(aba[['Analyte', 'CAS No.', 'Resultado']])
    else:
        # Para as abas subsequentes, pegue apenas a coluna 'Resultado'
        abas.append(aba[['Resultado']])

# Renomeie as colunas conforme necessário
for i, nome_aba in enumerate(nomes_abas):
    if i == 0:
        abas[i].columns = ['Analyte', 'Cas', f'{nome_aba}']
    else:
        abas[i].columns = [f'{nome_aba}']

# Concatene os DataFrames em um único DataFrame
dados_concatenados = pd.concat(abas, axis=1)

# Salve o resultado em um novo arquivo Excel
dados_concatenados.to_excel('Tabela Epa/Tabela_EPA.xlsx', index=False)
