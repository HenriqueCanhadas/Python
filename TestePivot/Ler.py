import pandas
import openpyxl
import xlwings

workbook = openpyxl.load_workbook('Ler/Export_Toyota_SBC_Geral.xlsx')

sheet = workbook['Amostras Resultados (2)']

print(f'Valores lidos em {sheet}:')

print(workbook)