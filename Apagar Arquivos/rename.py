import os
from datetime import datetime, timedelta


# Inicia o contador (data de início = data de hoje - 60 dias)
contador_data_start = -60

# Cria a data de start
data_hoje = datetime.today().date()
data_start = data_hoje + timedelta(days=contador_data_start)

# Inicializa as variáveis necessárias
data_start = datetime.now() - timedelta(days=60)  # Exemplo: começando 60 dias atrás
contador_dias = 1

teste1 = datetime.now()
teste2 = datetime.today().date()

print(teste1)
print(teste2)
