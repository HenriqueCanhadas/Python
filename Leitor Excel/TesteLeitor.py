import xlwings as xw
import openpyxl
from pathlib import Path

pasta = Path(__file__).resolve().parent

extensao_excel = '*.xlsx'

arquivos_excel = list(pasta.glob(extensao_excel))

arquivo = arquivos_excel[0]

wb_xlwings = xw.Book(arquivo)

valores_xlwings = []

linha=69

for sheet_name in wb_xlwings.sheets:

    planilha = wb_xlwings.sheets[sheet_name]

    condutividade = planilha.range('E41').value
    oxirreducao = planilha.range('G41').value
    oxigenio = planilha.range('I41').value
    ph = planilha.range('L41').value
    temperatura = planilha.range('N41').value
    turbidez = planilha.range('P41').value

    valores_xlwings.append((condutividade, oxirreducao, oxigenio, ph, temperatura, turbidez))

    print(f'Valores lidos em {sheet_name}:')
    print(f'Condutividade: {condutividade}')
    print(f'Potencial de oxirredução: {oxirreducao}')
    print(f'Oxigênio Dissolvido: {oxigenio}')
    print(f'pH: {ph}')
    print(f'Temperatura: {temperatura}')
    print(f'Turbidez: {turbidez}')
    print("-" * 100)

wb_xlwings.close()

workbook_openpyxl = openpyxl.load_workbook(arquivo)

for sheet_name in workbook_openpyxl.sheetnames:
    
    planilha_openpyxl = workbook_openpyxl[sheet_name]

    if len(valores_xlwings) > 0:
        condutividade, oxirreducao, oxigenio, ph, temperatura, turbidez = valores_xlwings.pop(0)

        planilha_openpyxl['E41'].value = condutividade
        planilha_openpyxl['G41'].value = oxirreducao
        planilha_openpyxl['I41'].value = oxigenio
        planilha_openpyxl['L41'].value = ph
        planilha_openpyxl['N41'].value = temperatura
        planilha_openpyxl['P41'].value = turbidez

    identificacao =planilha_openpyxl['C30'].value
    data =planilha_openpyxl['C6'].value
    horaensaio =planilha_openpyxl['H30'].value
    horaamostragem = planilha_openpyxl['K30'].value
    condicoes =planilha_openpyxl['P30'].value

    sheet = workbook_openpyxl['FINAL']

    sheet[f'A{linha}']=identificacao
    sheet[f'B{linha}']=data
    sheet[f'C{linha}']=horaensaio
    sheet[f'D{linha}']=horaamostragem
    sheet[f'E{linha}']=condutividade
    sheet[f'F{linha}']=oxirreducao
    sheet[f'G{linha}']=oxigenio
    sheet[f'H{linha}']=ph
    sheet[f'I{linha}']=temperatura
    sheet[f'J{linha}']=turbidez
    sheet[f'K{linha}']=condicoes

    workbook_openpyxl.save(arquivo)

    print(f'Escrevendo valores na linha:{linha}')

    linha+=1

    print(f'Identificação/Aba/Guia: {identificacao}')
    print(f'Data: {data}')
    print(f'Hora do ensaio: {horaensaio}')
    print(f'Hora da amostragem: {horaamostragem}')
    print(f'Condutividade: {condutividade}')
    print(f'Potencial de oxirredução: {oxirreducao}')
    print(f'Oxigênio Dissolvido: {oxigenio}')
    print(f'pH: {ph}')
    print(f'Temperatura: {temperatura}')
    print(f'Turbidez: {turbidez}')
    print(f'Condições ambientais: {condicoes}')

    print("-"*100)

    workbook_openpyxl.close()

print('Todos os dados foram escritos')

print("-"*100)