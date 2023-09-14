import openpyxl

# Abra o arquivo Excel
workbook = openpyxl.load_workbook("Tabelas\Arquivo.xlsx")

# Selecione a planilha desejada (pode ser por nome ou índice)
sheet = workbook["Tabelas\Arquivo.xlsx"]  # Ou use sheet = workbook[0] para selecionar a primeira planilha

# Valor que você deseja procurar na planilha
valor_procurado = 'Valor que você deseja encontrar'

# Percorra todas as linhas da planilha para encontrar a célula com o valor procurado
for row in sheet.iter_rows():
    for cell in row:
        if cell.value == valor_procurado:
            # Imprima a referência da célula onde o valor foi encontrado
            print("Valor encontrado em:", cell.coordinate)

# Feche o arquivo Excel
workbook.close()