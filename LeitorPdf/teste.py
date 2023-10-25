import openpyxl

workbook = openpyxl.load_workbook('LeitorPdf/arquivoteste.xlsx')

sheet = workbook['Table 2']

# Percorra as células da planilha e imprima o conteúdo se não estiver vazia
for row in sheet.iter_rows():
    for cell in row:
        if cell.value is not None:
            print(cell.value, end='\t')  # Imprime o valor da célula separado por tabulação
    print()  # Imprime uma nova linha após cada linha de células

# Feche o arquivo após a leitura
workbook.close()