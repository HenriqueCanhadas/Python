import os
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta

# Define o caminho onde a pasta será criada
caminho_base = r"C:\Users\henrique.canhadas\Desktop"
 
# Obtém a data de hoje formatada
data_hoje = datetime.today().strftime('%d-%m-%Y_%H´%M')
 
# Define o nome da pasta
nome_pasta = f"Amostras_{data_hoje}"
 
# Combina o caminho base e o nome da pasta
caminho_completo = os.path.join(caminho_base, nome_pasta)
 
# Cria a pasta com o nome formatado
os.makedirs(caminho_completo, exist_ok=True)
print(f"Pasta criada: {caminho_completo}")

# Inicia o serviço do ChromeDriveManager e instala a versão mais recente
servico = Service(ChromeDriverManager().install())

# Configurações GoogleChrome
opcoes_chrome = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": caminho_completo,
    "download.prompt_for_download": False,
    "directory_upgrade": True,
    "safebrowsing.enabled": True,
    "profile.default_content_settings.popups": 0,
    "profile.default_content_setting_values.automatic_downloads": 1
}

# Configura as opções do Google Chrome
opcoes_chrome.add_experimental_option("prefs", prefs)

# Definindo a variável que recebe o XPATH da mensagem de download em segundo plano
mensagem_segundo_plano = (By.XPATH, '//*[@id="1075"]/span') 

# Função para verificar se a mensagem está na tela
def mensagem_download(mensagem_segundo_plano):
    try:
        navegador.find_element(*mensagem_segundo_plano)
        return True
    except:
        return False

# Inicializa o navegador com as opções configuradas
navegador = webdriver.Chrome(service=servico, options=opcoes_chrome)
navegador.maximize_window()

# Acessa o site
navegador.get("https://labsoft-identitycenter-sts-prd.azurewebsites.net/Account/Login?ReturnUrl=%2Fconnect%2Fauthorize%2Fcallback%3Fclient_id%3DmyLIMSweb_JQuery%26redirect_uri%3Dhttps%253A%252F%252Foperator.mylimsweb.cloud%252Fcallback%252Findex%26response_type%3Dcode%26scope%3Dopenid%2520myLIMSweb_API_Create%2520myLIMSweb_API_Read%2520myLIMSweb_API_Update%2520myLIMSweb_API_Delete%2520DataViewer_API_Create%2520DataViewer_API_Read%2520DataViewer_API_Update%2520DataViewer_API_Delete%2520DataFactory_API_Create%2520DataFactory_API_Read%2520DataFactory_API_Update%2520DataFactory_API_Delete%26state%3D5d6e82bc61304a539eb558e4d12338df%26code_challenge%3DWMs1aUezfwUM-blX862r9-qXVhy9vgeQDopd1JCvTZI%26code_challenge_method%3DS256%26response_mode%3Dquery%26requesterClient%3Doperator")

# Adiciona um tempo de espera
tempo_espera = 30
wait = WebDriverWait(navegador, tempo_espera)

# Login
usuario = wait.until(EC.visibility_of_element_located((By.ID, "Username")))
usuario.send_keys("tvillavas")
senha = wait.until(EC.visibility_of_element_located((By.ID, "Password")))
senha.send_keys("Operator24")
botao_login = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "labsoft-login-button-primary")))
botao_login.click()

# Aguarda indefinidamente para manter a janela aberta
try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    # Fecha o navegador ao interromper o script com Ctrl+C
    navegador.quit()