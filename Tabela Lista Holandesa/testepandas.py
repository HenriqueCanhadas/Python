import pandas as pd

# Função para obter o valor correspondente em 'NAS' para um Analyte específico em uma aba
def obter_valor_nas(aba, analyte):
    try:
        return aba.loc[aba['Parâmetro'] == analyte, 'NAS'].values[0]
    except IndexError:
        return None

# Função para obter o valor correspondente em 'Máximo' para um Analyte específico em uma aba
def obter_valor_maximo(aba, analyte):
    try:
        return aba.loc[aba['Parâmetro'] == analyte, 'Máximo'].values[0]
    except IndexError:
        return None

# Leia cada aba da planilha original
aba_solo_agricola = pd.read_excel('Tabela Lista Holandesa/VROM_ListaHolandesa-VI-2013.xlsx', sheet_name='VROM-VI-2013_SoloAgricola')
aba_solo_residencial = pd.read_excel('Tabela Lista Holandesa/VROM_ListaHolandesa-VI-2013.xlsx', sheet_name='VROM-VI-2013_SoloResidencial')
aba_agua_subterranea = pd.read_excel('Tabela Lista Holandesa/VROM_ListaHolandesa-VI-2013.xlsx', sheet_name='VROM-VI-2013_AguaSubterranea')

# Extraia os valores únicos da coluna C de cada aba
valores_unicos_solo_agricola = aba_solo_agricola['Parâmetro'].unique()
valores_unicos_solo_residencial = aba_solo_residencial['Parâmetro'].unique()
valores_unicos_agua_subterranea = aba_agua_subterranea['Parâmetro'].unique()

# Combine todos os valores únicos em uma única lista e ordene-os alfabeticamente
valores_unicos_totais = sorted(set(valores_unicos_solo_agricola) | set(valores_unicos_solo_residencial) | set(valores_unicos_agua_subterranea))

# Crie um novo DataFrame com os valores únicos
df_resultado = pd.DataFrame({'Analyte': valores_unicos_totais})

# Adicione uma nova coluna 'Cas' com os valores correspondentes da coluna 'NAS' em cada aba
df_resultado['Cas'] = df_resultado['Analyte'].apply(lambda x: obter_valor_nas(aba_solo_agricola, x) or
                                                        obter_valor_nas(aba_solo_residencial, x) or
                                                        obter_valor_nas(aba_agua_subterranea, x))

# Adicione novas colunas 'Maximo_Agricola', 'Maximo_Residencial' e 'Maximo_Agua' com os valores correspondentes em 'Máximo' em cada aba
df_resultado['Solo Agricola'] = df_resultado['Analyte'].apply(lambda x: obter_valor_maximo(aba_solo_agricola, x))
df_resultado['Solo Residencial'] = df_resultado['Analyte'].apply(lambda x: obter_valor_maximo(aba_solo_residencial, x))
df_resultado['Agua Subterranea'] = df_resultado['Analyte'].apply(lambda x: obter_valor_maximo(aba_agua_subterranea, x))

# Ordene o DataFrame alfabeticamente pela coluna 'Analyte'
df_resultado = df_resultado.sort_values(by='Analyte')

# Salve o DataFrame em um novo arquivo Excel
df_resultado.to_excel('Tabela Lista Holandesa/Tabela_ListaHolandesa.xlsx', index=False)
