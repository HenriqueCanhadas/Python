import pathlib

# Obtenha o diretório atual
diretorio_atual = pathlib.Path()

# Extensão dos arquivos do Excel que você deseja localizar
extensao_excel = '*.xlsx'  # Altere para a extensão desejada, como '*.xls' se for um arquivo .xls

# Use o método glob para buscar os arquivos Excel no diretório atual
arquivos_excel = list(diretorio_atual.glob(extensao_excel))

if not arquivos_excel:
    print("Nenhum arquivo Excel encontrado no diretório atual.")
else:
    print("Arquivos Excel encontrados no diretório atual:")
    for arquivo in arquivos_excel:
        print(arquivo)