import openpyxl
import xlwings as xw

workbook = openpyxl.load_workbook('Relatorio\REVISÃO - Boletim de Amostragem 7918.xlsx')
wb = xw.Book('Relatorio\REVISÃO - Boletim de Amostragem 7918.xlsx')

n=70

for sheet_name in workbook.sheetnames:

    wb = xw.Book('Relatorio\REVISÃO - Boletim de Amostragem 7918.xlsx')
    
    planilha = wb.sheets[sheet_name]

    multiparametro=planilha.range('I14').value
    turbidimetro =planilha.range('I18').value
    identificacao =planilha.range('C30').value
    data =planilha.range('C6').value
    horaensaio =planilha.range('H30').value
    horaamostragem = planilha.range('K30').value
    condutividade = planilha.range('E41').value
    oxirreducao = planilha.range('G41').value
    oxigenio = planilha.range('I41').value
    ph = planilha.range('L41').value
    temperatura = planilha.range('N41').value
    turbidez = planilha.range('P41').value
    condicoes =planilha.range('P30').value

    

    sheet = workbook['FINAL']

    sheet[f'A{n}']= multiparametro
    sheet[f'B{n}']=turbidimetro
    sheet[f'C{n}']=identificacao
    sheet[f'D{n}']=data
    sheet[f'E{n}']= horaensaio
    sheet[f'F{n}']=horaamostragem
    sheet[f'G{n}']=condutividade
    sheet[f'H{n}']=oxirreducao
    sheet[f'I{n}']=oxigenio
    sheet[f'J{n}']=ph
    sheet[f'K{n}']=temperatura
    sheet[f'L{n}']=turbidez
    sheet[f'M{n}']=condicoes

    n+=1

    print(f'N esta em:{n}')

    workbook.save('Relatorio\REVISÃO - Boletim de Amostragem 7918.xlsx')
    wb.close()

    print(multiparametro)
    print(turbidimetro)
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





