import openpyxl

workbook = openpyxl.load_workbook('TestePivot/Tabela Cetesb/arquivoteste.xlsx')

sheet = workbook['Tabela']

teste = []

coordenada = []

nomes = [
    "INORGÂNICOS",
    "HIDROCARBONETOS AROMÁTICOS VOLÁTEIS",
    "HIDROCARBONETOS POLICÍCLICOS AROMÁTICOS",
    "BENZENOS CLORADOS",
    "ETANOS CLORADOS",
    "ETENOS CLORADOS",
    "METANOS CLORADOS",
    "FENÓIS CLORADOS",
    "FENÓIS NÃO CLORADOS",
    "ÉSTERES FTÁLICOS",
    "PESTICIDAS",
    "OUTROS",
    "VRQ – Valor de Referência de Qualidade; VP – Valor de Prevenção; VI – Valor de Intervenção"
]


# Percorra as células da planilha e imprima o conteúdo se não estiver vazia
for row in sheet.iter_rows():
    for cell in row:
        if cell.value is not None:
            #print(cell.value, end='\t')  # Imprime o valor da célula separado por tabulação
            pass
        if cell.value in nomes:
               teste.append(cell.value)
               coordenada.append(cell.coordinate)

print(teste)
print(coordenada)

intervalos = []

# Inicialize variáveis para rastrear o intervalo atual
inicio_intervalo = None

# Itere sobre os valores
for valor in coordenada:
    # Extraia as colunas e linhas
    coluna, linha = valor[0], int(valor[1:])
    
    # Verifique se o intervalo atual começou
    if inicio_intervalo is None:
        inicio_intervalo = (coluna, linha)
    # Verifique se o intervalo atual terminou
    elif linha > inicio_intervalo[1] + 1:
        coluna_atual, linha_atual = inicio_intervalo
        while linha_atual < linha:
            cell = sheet[f'{coluna_atual}{linha_atual}']
            print(cell.value)
            linha_atual += 1
        inicio_intervalo = (coluna, linha)

# Obtenha o número da última célula da lista
ultima_celula = coordenada[-1]
linha_ultima_celula = int(ultima_celula[1:])

# Imprima os valores da última linha
while linha_ultima_celula <= int(sheet[-1][1:]):
    cell = sheet[f'{coluna}{linha_ultima_celula}']
    print(cell.value)
    linha_ultima_celula += 1

''''
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
    if valor is None:
        break
    valores_coluna.append(valor)
    linha_inicial += 1

# Imprima os valores da coluna
print("Valores da coluna:")
for valor in valores_coluna:
    print(valor)
'''

# Feche o arquivo após a leitura
workbook.close()