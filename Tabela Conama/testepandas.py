import pandas as pd

# Carregue os dados das duas abas do Excel
try:
    aba1 = pd.read_excel('Tabela Conama/resolucao-conama-420-2009-gerenciamento-de-acs.xlsx', sheet_name='Table 2')
    aba2 = pd.read_excel('Tabela Conama/resolucao-conama-420-2009-gerenciamento-de-acs.xlsx', sheet_name='Table 3')
except FileNotFoundError:
    print("Arquivo não encontrado. Certifique-se de fornecer o caminho correto.")
    exit()
except Exception as e:
    print(f"Erro ao ler as abas do Excel: {e}")
    exit()

# Encontre o índice onde 'Inorgânicos' aparece na primeira coluna da aba1
indice_inorganicos_aba1 = aba1.index[aba1.iloc[:, 0] == 'Inorgânicos'][0]

# Encontre o índice onde 'Fenóis não clorados' aparece na primeira coluna da aba2
indice_fenois_aba2 = aba2.index[aba2.iloc[:, 0] == 'Fenóis não clorados'][0]

# Encontre o índice onde 'TOTAL' aparece na primeira coluna da aba2
indice_total_aba2 = aba2.index[aba2.iloc[:, 0] == 'TOTAL'][0]

# Ignore os valores específicos e pare de inserir dados quando encontrar o valor indicado
ignorar_valores = [
    'Inorgânicos',
    'Hidrocarbonetos aromáticos voláteis',
    'Hidrocarbonetos policíclicos aromáticos',
    'Benzenos clorados',
    'Etanos clorados',
    'Etenos clorados',
    'Metanos clorados',
    'Fenóis clorados',
    'Fenóis não clorados',
    'Ésteres ftálicos',
    'Pesticidas organoclorados',
    'PCBs'
]

# Extraia os valores da primeira coluna a partir dos índices encontrados, ignorando valores específicos
coluna_aba1 = aba1.iloc[indice_inorganicos_aba1:, 0].loc[~aba1.iloc[indice_inorganicos_aba1:, 0].isin(ignorar_valores)]
coluna_aba2 = aba2.iloc[indice_fenois_aba2:indice_total_aba2 + 1, 0].loc[~aba2.iloc[indice_fenois_aba2:indice_total_aba2 + 1, 0].isin(ignorar_valores)]

# Combine as duas colunas em um novo DataFrame
novo_dataframe = pd.DataFrame({
    'Analyte': pd.concat([coluna_aba1, coluna_aba2], ignore_index=True)
})

# Carregue os dados do Excel anterior
try:
    excel_anterior_aba2 = pd.read_excel('Tabela Conama/resolucao-conama-420-2009-gerenciamento-de-acs.xlsx', sheet_name='Table 3')
    excel_anterior_aba1 = pd.read_excel('Tabela Conama/resolucao-conama-420-2009-gerenciamento-de-acs.xlsx', sheet_name='Table 2')
except FileNotFoundError:
    print("Arquivo não encontrado. Certifique-se de fornecer o caminho correto.")
    exit()
except Exception as e:
    print(f"Erro ao ler o Excel anterior: {e}")
    exit()

# Renomeie as colunas para torná-las mais legíveis
excel_anterior_aba1 = excel_anterior_aba1.rename(columns={
    'ANEXO II\nLISTA DE VALORES ORIENTADORES PARA SOLOS E PARA ÁGUAS SUBTERRÂNEAS': 'Substâncias',
    'Unnamed: 1': 'CAS n°',  # Substitua 'Unnamed: 1' pelo rótulo correto
    'Unnamed: 2': 'Solo (mg.kg-1 de peso seco) (1)',
    'Unnamed: 3': 'Prevenção',
    'Unnamed: 4': 'Agrícola APMax',
    'Unnamed: 5': 'Residencial',
    'Unnamed: 6': 'Industrial',
    'Unnamed: 7': 'Investigação'
})

# Renomeie as colunas para torná-las mais legíveis
excel_anterior_aba2 = excel_anterior_aba2.rename(columns={
    'ANEXO II\nLISTA DE VALORES ORIENTADORES PARA SOLOS E PARA ÁGUAS SUBTERRÂNEAS': 'Substâncias',
    'Unnamed: 1': 'CAS n°',
    'Unnamed: 2': 'Solo (mg.kg-1 de peso seco) (1)',
    'Unnamed: 3': 'Prevenção',
    'Unnamed: 4': 'Agrícola APMax',
    'Unnamed: 5': 'Residencial',
    'Unnamed: 6': 'Industrial',
    'Água Subterrâ nea (µg.L-1)': 'Investigação'  # Corrigir o nome da coluna
})

# Use os índices das colunas para mapear valores das colunas específicas no Excel anterior
colunas_comparacao = ['CAS n°','Prevenção', 'Agrícola APMax', 'Residencial', 'Industrial', 'Investigação']
mapeamento_colunas_aba1 = {coluna: dict(zip(excel_anterior_aba1['Substâncias'], excel_anterior_aba1[coluna])) for coluna in colunas_comparacao}
mapeamento_colunas_aba2 = {coluna: dict(zip(excel_anterior_aba2['Substâncias'], excel_anterior_aba2[coluna])) for coluna in colunas_comparacao}

# Combine os mapeamentos das duas abas
mapeamento_colunas = {coluna: {**mapeamento_colunas_aba1[coluna], **mapeamento_colunas_aba2[coluna]} for coluna in colunas_comparacao}

# Crie novas colunas nas colunas específicas no novo DataFrame usando os mapeamentos
for coluna in colunas_comparacao:
    novo_dataframe[coluna] = novo_dataframe['Analyte'].map(mapeamento_colunas[coluna])

# Renomeie as colunas do DataFrame antes de salvar no Excel
novo_dataframe = novo_dataframe.rename(columns={
    'CAS n°': 'CAS',
    'Prevenção': 'Solo Prevenção',
    'Agrícola APMax': 'Solo Agricola',
    'Residencial': 'Solo Residencial',
    'Industrial': 'Solo Industrial',
    'Investigação': 'Agua Subterranea'
})

novo_dataframe.to_excel('Tabela Conama/Tabela_Conama.xlsx', index=False)