import os
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

# Obter a data de hoje no formato 'YYYY-MM-DD'
data_hoje = datetime.today().strftime('%d-%m-%Y')

# Definir o caminho base onde a pasta do dia será criada
caminho_base = r"C:\Users\henrique.canhadas\OneDrive - Servmar Ambientais\Documentos\Codigos\GitHub\Python\0-Relatorios-0\Teste"

# Combinar o caminho base com a data de hoje para formar o caminho completo do diretório do dia
pasta_dia = os.path.join(caminho_base, data_hoje)

# Verificar se a pasta do dia já existe, se não, criar
if not os.path.exists(pasta_dia):
    os.makedirs(pasta_dia)
    print(f"Pasta do dia criada: {pasta_dia}")
else:
    print(f"A pasta do dia {pasta_dia} já existe.")

# Obter o horário atual no formato 'HH.MM'
horario = datetime.today().strftime('%H.%M')

# Definir o nome da nova pasta a ser criada dentro da pasta do dia
nome_pasta = f"Relátorio_3_{horario}"

# Combinar o caminho da pasta do dia com o nome da nova pasta
caminho_completo = os.path.join(pasta_dia, nome_pasta)

# Verificar se a nova pasta já existe, se não, criar
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

# Acessa a aba "Relatórios Gerenciais"
relatorios_gerenciais = wait.until(EC.visibility_of_element_located((By.ID, "sectionitem_15")))
relatorios_gerenciais.click()
time.sleep(10)
relatorios_gerenciais = wait.until(EC.visibility_of_element_located((By.ID, "sectionitem_15")))
relatorios_gerenciais.click()
time.sleep(10)
#Seleção de Amostras
botao_selecao_amostras = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "k-select")))
botao_selecao_amostras.click()
time.sleep(3)
#Seleção Amostras - Métodos de Análises
amostras_metodos_analises = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ComboBox_47_listbox"]/li[15]')))
amostras_metodos_analises.click()
time.sleep(3)
#Adicionar Situação Recebia
botao_adicionar = wait.until(EC.visibility_of_element_located((By.ID, "button_70")))
botao_adicionar.click()
time.sleep(3)
recebida = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="Grid_127_noteditable"]/div[2]/table/tbody/tr[2]/td[2]')))
recebida.click()
time.sleep(3)
botao_selecionar = wait.until(EC.visibility_of_element_located((By.ID, "button_122")))
botao_selecionar.click()
time.sleep(3)
#Adicionar Situação em Analise
botao_adicionar = wait.until(EC.visibility_of_element_located((By.ID, "button_70")))
botao_adicionar.click()
time.sleep(3)
analise = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="Grid_146_noteditable"]/div[2]/table/tbody/tr[3]/td[2]')))
analise.click()
time.sleep(3)
botao_selecionar = wait.until(EC.visibility_of_element_located((By.ID, "button_141")))
botao_selecionar.click()
time.sleep(3)

# Definindo a variável que recebe o XPATH da mensagem de download em segundo plano
mensagem_segundo_plano = (By.ID, "1059")

# Função para verificar se a mensagem de download está na tela
def mensagem_download(driver, mensagem_segundo_plano):
    try:
        driver.find_element(*mensagem_segundo_plano)
        print("Mensagem de download presente, aguardando...")
        time.sleep(2)
        return True
    except:
        return False

# Função para monitorar mudanças no HTML de um elemento
def monitorar_mudanca_html(driver, elemento_id, mensagem_segundo_plano):
    time.sleep(3)    
    # Aguarda enquanto a mensagem de download em segundo plano estiver presente
    while mensagem_download(driver, mensagem_segundo_plano):
        pass
    # Loop para monitorar mudanças no HTML do botão
    while True:
        # Re-localiza o botão para garantir que estamos capturando o estado atualizado
        button = driver.find_element(By.ID, elemento_id)
        html_atual = button.get_attribute('outerHTML')
        print("HTML ATUAL:")
        print(html_atual)
        # Verifique se "disabled" está presente no HTML do botão
        if '"disabled"' in html_atual:
            print("Botão ainda está desabilitado, continuando a monitorar...")
            print("HTML RECEBIDO:")
            print(html_atual)
            time.sleep(2)  # Pequeno delay para não sobrecarregar o sistema
            continue  # Retorna ao início do loop para verificar novamente
        else:
            print("Botão habilitado, saindo do loop!")
            print("HTML RECEBIDO:")
            print(html_atual)
            break  # Interrompe o loop quando o botão estiver habilitado

#Clicar em Gerar Relatorio
time.sleep(5)
gerar_relatorio = wait.until(EC.visibility_of_element_located((By.ID, 'button_10')))
gerar_relatorio.click()
time.sleep(0.5)

# Chame a função para monitorar mudanças no botão com ID 'button_10'
while monitorar_mudanca_html(navegador, 'button_10',mensagem_segundo_plano):
    pass

time.sleep(10)
#Sair do Mylims
icone_logout = wait.until(EC.visibility_of_element_located((By.ID, 'Logout')))
icone_logout.click()
time.sleep(10)

'''
# Aguarda indefinidamente para manter a janela aberta
try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    # Fecha o navegador ao interromper o script com Ctrl+C
    navegador.quit()
'''