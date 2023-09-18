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

