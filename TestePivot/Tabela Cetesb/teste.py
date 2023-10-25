import openpyxl

workbook = openpyxl.load_workbook('TestePivot/Tabela Cetesb/arquivoteste.xlsx')

sheet = workbook['Table 2']
'''
# Percorra as células da planilha e imprima o conteúdo se não estiver vazia
for row in sheet.iter_rows():
    for cell in row:
        if cell.value is not None:
            print(cell.value, end='\t')  # Imprime o valor da célula separado por tabulação
    print()  # Imprime uma nova linha após cada linha de células
'''

# Especifique a coluna que você deseja ler
coluna = 'O'  # Substitua 'A' pela letra da coluna que você deseja ler

# Especifique a linha de partida
linha_inicial = 7  # Substitua pela linha de partida desejada

# Inicialize uma lista para armazenar os valores da coluna
valores_coluna = []

# Loop para ler os valores da coluna até encontrar 'NONE'
while True:
    celula = sheet[f'{coluna}{linha_inicial}']
    valor = celula.value
    if valor is None or valor == 'NONE':
        break
    valores_coluna.append(valor)
    linha_inicial += 1

# Imprima os valores da coluna
print("Valores da coluna:")
for valor in valores_coluna:
    print(valor)


# Feche o arquivo após a leitura
workbook.close()