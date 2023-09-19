import xlwings as xw
import openpyxl

wb_xlwings = xw.Book('Relatorio\REVISÃO - Boletim de Amostragem 7918.xlsx')

valores_xlwings = []

n=70

nomes_das_guias = [sheet.name for sheet in wb_xlwings.sheets]


for sheet_name in wb_xlwings.sheets:

    # Acessar a planilha atual com xlwings
    planilha = wb_xlwings.sheets[sheet_name]

    # Ler os valores das células com xlwings
    condutividade = planilha.range('E41').value
    oxirreducao = planilha.range('G41').value
    oxigenio = planilha.range('I41').value
    ph = planilha.range('L41').value
    temperatura = planilha.range('N41').value
    turbidez = planilha.range('P41').value

    valores_xlwings.append((condutividade, oxirreducao, oxigenio, ph, temperatura, turbidez))

    # Imprimir os valores

    print(f'Valores lidos em {sheet_name}:')
    print(f'Condutividade: {condutividade}')
    print(f'Oxirreducao: {oxirreducao}')
    print(f'Oxigenio: {oxigenio}')
    print(f'pH: {ph}')
    print(f'Temperatura: {temperatura}')
    print(f'Turbidez: {turbidez}')
    print("-" * 50)

    # Fechar o arquivo Excel com xlwings após o loop
wb_xlwings.close()

workbook_openpyxl = openpyxl.load_workbook('Relatorio\REVISÃO - Boletim de Amostragem 7918.xlsx')

for sheet_name in workbook_openpyxl.sheetnames:
    planilha_openpyxl = workbook_openpyxl[sheet_name]

    # Agora você pode acessar os valores da lista e usá-los em openpyxl
    if len(valores_xlwings) > 0:
        condutividade, oxirreducao, oxigenio, ph, temperatura, turbidez = valores_xlwings.pop(0)

        # Escrever os valores em openpyxl
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

    sheet[f'A{n}']=identificacao
    sheet[f'B{n}']=data
    sheet[f'C{n}']=horaensaio
    sheet[f'D{n}']=horaamostragem
    sheet[f'E{n}']=condutividade
    sheet[f'F{n}']=oxirreducao
    sheet[f'G{n}']=oxigenio
    sheet[f'H{n}']=ph
    sheet[f'I{n}']=temperatura
    sheet[f'J{n}']=turbidez
    sheet[f'K{n}']=condicoes

    workbook_openpyxl.save('Relatorio\REVISÃO - Boletim de Amostragem 7918.xlsx')

    print(f'N esta em:{n}')

    n+=1

    print(identificacao)
    print(data)
    print(horaensaio)
    print(horaamostragem)
    print(condutividade)
    print(oxirreducao)
    print(oxigenio)
    print(ph)
    print(temperatura)
    print(turbidez)
    print(condicoes)

    print("-"*50)

    workbook_openpyxl.close()