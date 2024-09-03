# Obter o número do relatório e o horário atual
from datetime import datetime


numero_relatorio = 1
horario = datetime.today().strftime('%H.%M')

# Formatar o nome da pasta de maneira clara e descritiva
pasta_horario = f"Relatório_{numero_relatorio:02d}_CriadoÀs_{horario.replace('.', 'h')}min"

print(pasta_horario)
