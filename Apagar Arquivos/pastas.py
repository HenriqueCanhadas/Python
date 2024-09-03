import os
from datetime import datetime

# Define o caminho onde a pasta será criada
caminho_base = r"C:\Users\henrique.canhadas\OneDrive - Servmar Ambientais\Documentos\Codigos\GitHub\Python\Apagar Arquivos\Teste Apagar"

# Obtém a data de hoje e formata como dd-mm-yyyy HH´MM
data_hoje = datetime.today().strftime('%d-%m-%Y_%H´%M')

# Define o nome da pasta
nome_pasta = f"Amostras_{data_hoje}"

# Combina o caminho base e o nome da pasta
caminho_completo = os.path.join(caminho_base, nome_pasta)

# Cria a pasta
os.makedirs(caminho_completo, exist_ok=True)

print(f"Pasta criada: {caminho_completo}")
