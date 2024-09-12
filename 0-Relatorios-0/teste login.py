import os
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def iniciar_navegador(url_labsoft):
    # Inicia o serviço do ChromeDriverManager e instala a versão mais recente
    servico = Service(ChromeDriverManager().install())

    # Configurações do Google Chrome
    opcoes_chrome = webdriver.ChromeOptions()
    prefs = {
        "download.prompt_for_download": False,
        "directory_upgrade": True,
        "safebrowsing.enabled": True,
        "profile.default_content_settings.popups": 0,
        "profile.default_content_setting_values.automatic_downloads": 1
    }

    opcoes_chrome.add_experimental_option("prefs", prefs)
    
    # Inicializa o navegador com as opções configuradas
    navegador = webdriver.Chrome(service=servico, options=opcoes_chrome)

    # Maximiza a janela
    navegador.maximize_window()

    # Acessa o site especificado
    navegador.get(url_labsoft)

    # Tempo de espera para o carregamento completo
    espera = WebDriverWait(navegador, 30)
    
    return navegador, espera

def login(usuario, senha, espera):
    # Realiza o login
    campo_login = espera.until(EC.visibility_of_element_located((By.ID, "Username")))
    campo_login.clear()  # Limpa o campo antes de inserir o texto
    campo_login.send_keys(usuario)
    
    campo_senha = espera.until(EC.visibility_of_element_located((By.ID, "Password")))
    campo_senha.clear()  # Limpa o campo antes de inserir o texto
    campo_senha.send_keys(senha)
    
    botao_login = espera.until(EC.visibility_of_element_located((By.CLASS_NAME, "labsoft-login-button-primary")))
    botao_login.click()

    print("Login realizado com sucesso.")

def logout(navegador, espera):
    time.sleep(3)
    # Sair do Mylims usando clique via JavaScript
    icone_logout = espera.until(EC.presence_of_element_located((By.ID, 'Logout')))
    navegador.execute_script("arguments[0].click();", icone_logout)
    time.sleep(10)
    print("Logout realizado com sucesso.")

def main():
    url_labsoft = "https://labsoft-identitycenter-sts-prd.azurewebsites.net/Account/Login?ReturnUrl=%2Fconnect%2Fauthorize%2Fcallback%3Fclient_id%3DmyLIMSweb_JQuery%26redirect_uri%3Dhttps%253A%252F%252Foperator.mylimsweb.cloud%252Fcallback%252Findex%26response_type%3Dcode%26scope%3Dopenid%2520myLIMSweb_API_Create%2520myLIMSweb_API_Read%2520myLIMSweb_API_Update%2520myLIMSweb_API_Delete%2520DataViewer_API_Create%2520DataViewer_API_Read%2520DataViewer_API_Update%2520DataViewer_API_Delete%2520DataFactory_API_Create%2520DataFactory_API_Read%2520DataFactory_API_Update%2520DataFactory_API_Delete%26state%3D5d6e82bc61304a539eb558e4d12338df%26code_challenge%3DWMs1aUezfwUM-blX862r9-qXVhy9vgeQDopd1JCvTZI%26code_challenge_method%3DS256%26response_mode%3Dquery%26requesterClient%3Doperator"
    usuario = "tvillavas"
    senha = "Operator24"
    
    # Inicia o navegador e espera
    navegador, espera = iniciar_navegador(url_labsoft)
    contador = 0

    try:
        while True:
            # Tenta fazer login
            login(usuario, senha, espera)
            logout(navegador, espera)
            contador += 1
            print(f"Login e logout número {contador} concluído com sucesso.")
            time.sleep(3)  # Aguarda alguns segundos antes de tentar novamente
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        # Fecha o navegador após finalizar
        navegador.quit()

if __name__ == "__main__":
    main()
