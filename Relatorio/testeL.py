import openpyxl
import pandas as pd

import xlwings as xw

# Abra o arquivo Excel
wb = xw.Book('Relatorio\REVISÃO - Boletim de Amostragem 7918.xlsx')  # Substitua 'exemplo.xlsx' pelo nome do seu arquivo Excel

# Acesse a planilha desejada
planilha = wb.sheets['PMN-03']  # Substitua 'Planilha1' pelo nome da sua planilha

# Acesse o valor da célula com formatação (por exemplo, A1)
valor_celula = planilha.range('E41').value

# Feche o arquivo Excel
wb.close()

# Imprima o valor
print(f'O valor formatado da célula é: {valor_celula}')

#----------------------------------------------------------------------------------------------


import openpyxl

# Abra o arquivo Excel
workbook = openpyxl.load_workbook('Relatorio\REVISÃO - Boletim de Amostragem 7918.xlsx')  # Substitua 'exemplo.xlsx' pelo nome do seu arquivo Excel

# Selecione a planilha desejada
planilha = workbook['PMN-03']  # Substitua 'Planilha1' pelo nome da sua planilha

# Acesse a célula desejada (por exemplo, A1)
célula = planilha['E41']  # Substitua 'A1' pela célula que você deseja

# Forçar o cálculo da fórmula na célula
workbook.calculation.on_change(célula)

# Obtenha o valor da célula, que é o resultado da fórmula
valor_celula = célula.value

# Feche o arquivo Excel
workbook.close()

# Imprima o valor da célula
print(f'O valor da célula é: {valor_celula}')
