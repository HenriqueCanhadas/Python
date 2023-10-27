import openpyxl
from datetime import datetime

workbook = openpyxl.load_workbook('Tabela Cetesb/arquivoteste.xlsx')

sheet = workbook['Tabela']

linhaParaTerminal = ("*"*206)

nomes_parametros = []

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
    "VRQ – Valor de Referência de Qualidade; VP – Valor de Prevenção; VI – Valor de Intervenção",
]

for row in sheet.iter_rows():
    for cell in row:
        if cell.value is not None:
            for nome in nomes:
                if nome.lower() in str(cell.value).lower():
                    nomes_parametros.append(cell.value)
                    coordenada.append(cell.coordinate)

first_coord = coordenada[0]
last_coord = coordenada[-1]

start_cell = sheet[first_coord]
end_cell = sheet[last_coord]

nomes_quimicos = []  # Lista para armazenar os valores das células no intervalo

for row in sheet.iter_rows(min_row=start_cell.row, max_row=end_cell.row, min_col=start_cell.column, max_col=end_cell.column):
    for cell in row:
            if cell.value is not None:
                if "VRQ – Valor de Referência de Qualidade; VP – Valor de Prevenção; VI – Valor de Intervenção" in str(cell.value):
                    break  # Para o loop interno
            nomes_quimicos.append(cell.value)

# Inicialize uma lista para armazenar os valores da coluna B
cas = []

# Comece a partir da célula B7
for row in sheet.iter_rows(min_row=7, max_row=sheet.max_row, min_col=2, max_col=4):  # Altere max_col para 10
    for cell in row:
        # Verifique se o valor da coluna B é None
        if cell.column == 2:  # Coluna B
            #if cell.value and (cell.value is None or not isinstance(cell.value, datetime.datetime())):
            if not isinstance(cell.value, datetime.datetime):
                # Encontre o próximo valor nas colunas C (3) e D (4) na mesma linha
                valor_coluna_C = None
                valor_coluna_D = None
                for i in range(1, len(row)):
                    if row[i].column == 3:  # Coluna C
                        valor_coluna_C = row[i].value
                    elif row[i].column == 4:  # Coluna D
                        valor_coluna_D = row[i].value

                # Escolha entre o valor da coluna C ou D
                if valor_coluna_C is not None:
                    cas.append(valor_coluna_C)
                elif valor_coluna_D is not None:
                    cas.append(valor_coluna_D)
            else:
                cas.append(cell.value)


# Inicialize uma lista para armazenar os valores da coluna H
valores_coluna_H = []

# Comece a partir da célula H7
for row in sheet.iter_rows(min_row=7, max_row=sheet.max_row, min_col=8, max_col=10):  # Altere max_col para 10
    for cell in row:
        # Verifique se o valor da coluna H é None
        if cell.column == 8:  # Coluna H
            if cell.value is None:
                # Encontre o próximo valor nas colunas I (9) e J (10) na mesma linha
                valor_coluna_I = None
                valor_coluna_J = None
                for i in range(1, len(row)):
                    if row[i].column == 9:  # Coluna I
                        valor_coluna_I = row[i].value
                    elif row[i].column == 10:  # Coluna J
                        valor_coluna_J = row[i].value

                # Escolha entre o valor da coluna I ou J
                if valor_coluna_I is not None:
                    valores_coluna_H.append(valor_coluna_I)
                elif valor_coluna_J is not None:
                    valores_coluna_H.append(valor_coluna_J)
            else:
                valores_coluna_H.append(cell.value)

# Agora, valores_coluna_H contém todos os valores da coluna H, considerando a condição

print(linhaParaTerminal)

print(valores_coluna_H)

quantidadeH = len(valores_coluna_H)

print(quantidadeH)

print(linhaParaTerminal)

print(cas)

quantidadeb = len(cas)

print(quantidadeb)

print(linhaParaTerminal)

''''
for i in range(0, len(coordenada), 2):
    coord_inicio = coordenada[i]
    coord_fim = coordenada[i + 1]

    start_cell = sheet[coord_inicio]
    end_cell = sheet[coord_fim]

    for row in sheet.iter_rows(min_row=start_cell.row, max_row=end_cell.row, min_col=start_cell.column, max_col=end_cell.column):
        for cell in row:
            if cell.value is not None:
                if "VRQ – Valor de Referência de Qualidade; VP – Valor de Prevenção; VI – Valor de Intervenção" in str(cell.value):
                    break  # Para o loop interno
                else:
                    print(cell.value)
'''
'''
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