from datetime import datetime, timedelta
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Inicializa as variáveis necessárias
data_start = datetime.now() - timedelta(days=60)  # Exemplo: começando 60 dias atrás
contador_dias = 1

# Lista para armazenar os períodos
periodos = []

# Pega o período dos últimos 60 dias e baixa os arquivos no intervalo de 2 em 2
while contador_dias <= 60:
    data_inicio = data_start + timedelta(days=contador_dias - 1)
    data_final = data_start + timedelta(days=contador_dias)
    data_inicio_str = data_inicio.strftime('%d/%m/%Y') + " 00:01"
    data_final_str = data_final.strftime('%d/%m/%Y') + " 23:59"

    print(f"Data1: {data_inicio_str}")
    print(f"Data2: {data_final_str}")
    print("****************************")

    # Adiciona o período na lista
    periodos.append(f"{data_inicio_str} - {data_final_str}")

    contador_dias = contador_dias + 2

print("Terminou")

# Exibe os períodos salvos
print(periodos)

print(f"Tamanho da lista de períodos: {len(periodos)}")
