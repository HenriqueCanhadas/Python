from pathlib import Path

# Caminho para a pasta atual onde o script Python está localizado
pasta = Path(__file__).resolve().parent

# Extensão dos arquivos do Excel que você deseja localizar
extensao_excel = '*.xlsx'  # Altere para a extensão desejada, como '*.xls' se for um arquivo .xls

# Use o método glob para buscar todos os arquivos Excel na pasta atual
arquivos_excel = list(pasta.glob(extensao_excel))

# Verifique se há pelo menos um arquivo Excel na lista
if arquivos_excel:
    # Se houver mais de um arquivo, você pode escolher um específico, como o primeiro da lista
    arquivo = arquivos_excel[0]
    print(f"Arquivo Excel encontrado: {arquivo}")
else:
    print("Nenhum arquivo Excel encontrado na pasta atual.")