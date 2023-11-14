import openpyxl
import pandas as pd

import xlrd


excel_laboratorio=openpyxl.load_workbook('Ceimic/Analise Ceimic.xlsx')

planilha=excel_laboratorio['Amostras Resultados']

Teste = []

pm = []  # antigo id
tipo_de_amostra = []  # antigo tipo
data_hora = []  # antiga data
'''
for item in planilha.iter_rows(1, planilha.max_row, min_col=1, max_col=6):
    for celula in item:
        if celula.value is not None:
         print(celula.value)
         Teste.append(celula.value)
'''
for linha in range(2, planilha.max_row + 1):
        celula_pm = planilha.cell(row=linha, column=5).value  # Antiga cell1
        celula_seguinte = planilha.cell(row=linha+1, column=5).value  # Antiga cell2

        if celula_pm is not None and (celula_seguinte is None or celula_pm != celula_seguinte):
            pm.append(planilha.cell(row=linha, column=5).value)
            tipo_de_amostra.append(planilha.cell(row=linha, column=6).value)
            data_hora.append(planilha.cell(row=linha, column=6).value)

print(pm)

analises={}
resultado={}

for linha in range(2, planilha.max_row + 1):
        # Valor da coluna 'A' IDENTIFICAÇÃO DA AMOSTRA
        celula_pm = planilha.cell(row=linha, column=5).value
        # Valor da coluna 'D' ANALISE
        celula_analise = planilha.cell(row=linha, column=14).value
        # Valor da coluna 'E' RESULTADO
        celula_resultado = planilha.cell(row=linha, column=15).value
        # Valor da coluna 'F' UNIDADE
        celula_unidade = planilha.cell(row=linha, column=16).value

        # Check if celula_pm is not None and at least one of the analysis-related cells is not None
        if celula_pm is not None and (celula_analise is not None or celula_resultado is not None or celula_unidade is not None):
            # If the key (celula_pm) is not in analises, initialize it as an empty list
            if celula_pm not in analises:
                analises[celula_pm] = []
                resultado[celula_pm] = []

            analises[celula_pm].append(celula_analise)
            resultado[celula_pm].append([celula_resultado,celula_unidade])

print(analises['BV-04'])

quantidade_itens_bv_03 = len(analises['BV-04'])
print(f"Quantidade de itens: {quantidade_itens_bv_03}")

excel_laboratorio.close()

print("teste")

import pandas as pd
import openpyxl
 
tabela_lab = pd.read_excel('Ceimic/SERVMAR_Edd-14-11-23.xlsx')
tabela_bd = pd.read_excel('Ceimic/VSs das amostras - Servmar.xlsx')
 
procv = pd.merge(tabela_lab, tabela_bd,how='left', on="Análise")
print(procv)
 
procv.to_excel('Ceimic\Resultado_Merge_teste.xlsx', index=False)


'''
# Carregar a planilha
workbook = openpyxl.load_workbook('Ceimic/Parametros Ceimic.xlsx')

# Selecionar a primeira folha da planilha
sheet = workbook.active
# Inicializar a lista para armazenar os valores encontrados
valores_encontrados = []
# Iterar sobre as linhas da planilha
for row in sheet.iter_rows(min_row=2, values_only=True):  # Começa da segunda linha para evitar cabeçalhos
    # Verificar se o valor da célula está presente no dicionário
    if row[1] in analises:
          valores_encontrados.append((row[0],row[1] ,row[2]))  # Adicionar o valor da primeira coluna à lista

quantidade_itens = len(valores_encontrados)
print(f"Quantidade de itens: {quantidade_itens}")

# Fechar a planilha
workbook.close()
'''