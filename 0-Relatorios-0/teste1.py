from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
import os

# Define o user-agent
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0'

# Caminho para o msedgedriver.exe
edge_driver_path = os.path.join(os.getcwd(), 'msedgedriver.exe')

# Configuração do serviço do Edge
edge_service = Service(edge_driver_path)

# Opções do Edge
edge_options = Options()
edge_options.add_argument(f'user-agent={user_agent}')

# Inicializa o navegador Edge com o serviço e as opções
browser = webdriver.Edge(service=edge_service, options=edge_options)

# Abre a página desejada
browser.get('https://python.org')

# Mantém o navegador aberto
input("Pressione Enter para fechar o navegador...")
