#import pandas as pd
#
## Lê a tabela "Analise Ceimic.xlsx" e a tabela "banco de dados - CEIMIC.xlsx"
#tabela_lab = pd.read_excel('Ceimic/Analise Ceimic.xlsx')
#tabela_bd = pd.read_excel('Ceimic/banco de dados - ceimic.xlsx')
#
## Pega todos os itens que tem em comum em relação a coluna "Análise", junta em uma planilha só e salva como "Resultado_Merge.xlsx"
#procv = pd.merge(tabela_lab, tabela_bd, how='left', on="Análise")
#procv.to_excel('Ceimic/Resultado_Merge.xlsx', index=False)
#data_frame = pd.read_excel('Ceimic/Resultado_Merge.xlsx')
#
## Pega da coluna "SAMPLENAME" todos os pms e pega da coluna "Descrição Método" todos as descrições dos métodos (pega os valores unicos e joga na lista) 
#lista_pm = data_frame['SAMPLENAME'].unique()
#lista_descricao_metodo = data_frame['Descrição Método'].unique()
#
## Criar um novo DataFrame para armazenar os resultados filtrados
#resultado_final = pd.DataFrame()
#
## Iterar sobre as listas e adicionar os resultados filtrados ao novo DataFrame
#for pm in lista_pm:
#    for descricao_metodo in lista_descricao_metodo:
#        filtro = (data_frame['SAMPLENAME'] == pm) & (data_frame['Descrição Método'] == descricao_metodo)
#        resultado_filtrado = data_frame[filtro]
#        
#        # Verificar se o resultado não está vazio antes de adicionar ao DataFrame final
#        if not resultado_filtrado.empty:
#            resultado_final = resultado_final.append(resultado_filtrado[["SAMPLENAME", "SAMPDATE", "Descrição Método", "Análise", "CASNUMBER", "Result", "UNITS"]], ignore_index=True)
#
#resultado_final.to_excel('Ceimic/Resultado_Final.xlsx', index=False)
#


import pandas as pd

# Lê a tabela "Analise Ceimic.xlsx" e a tabela "banco de dados - CEIMIC.xlsx"
tabela_lab = pd.read_excel('Ceimic/Analise Ceimic.xlsx')
tabela_bd = pd.read_excel('Ceimic/banco de dados - ceimic.xlsx')

# Pega todos os itens que têm em comum em relação à coluna "Análise", junta em uma planilha só e salva como "Resultado_Merge.xlsx"
procv = pd.merge(tabela_lab, tabela_bd, how='left', on="Análise")
procv.to_excel('Ceimic/Resultado_Merge.xlsx', index=False)
data_frame = pd.read_excel('Ceimic/Resultado_Merge.xlsx')

# Pega da coluna "SAMPLENAME" todos os PMs e pega da coluna "Descrição Método" todas as descrições dos métodos (pega os valores únicos e joga na lista)
lista_pm = data_frame['SAMPLENAME'].unique()
lista_descricao_metodo = data_frame['Descrição Método'].unique()

# Criar um novo DataFrame para armazenar os resultados filtrados
colunas_resultado_final = ["SAMPLENAME", "SAMPDATE", "Descrição Método", "Análise", "CASNUMBER", "Result", "UNITS"]
resultado_final = pd.DataFrame(columns=colunas_resultado_final)

# Iterar sobre as listas e adicionar os resultados filtrados ao novo DataFrame
for pm in lista_pm:
    for descricao_metodo in lista_descricao_metodo:
        filtro = (data_frame['SAMPLENAME'] == pm) & (data_frame['Descrição Método'] == descricao_metodo)
        resultado_filtrado = data_frame.loc[filtro, colunas_resultado_final]
        
        # Verificar se o resultado não está vazio antes de adicionar ao DataFrame final
        if not resultado_filtrado.empty:
            resultado_final = pd.concat([resultado_final, resultado_filtrado], ignore_index=True)

resultado_final.to_excel('Ceimic/Resultado_Final.xlsx', index=False)
