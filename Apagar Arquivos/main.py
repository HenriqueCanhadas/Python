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
caminho_base = r"C:\Users\henrique.canhadas\Desktop\Teste"

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

# Coloca os inputs solicitados
botao_selecao_amostras = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "k-select")))
botao_selecao_amostras.click()
time.sleep(3)
amostras_informacoes_analises = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ComboBox_47_listbox"]/li[12]')))
amostras_informacoes_analises.click()
time.sleep(3)
botao_selecao_registrada = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="layoutrow_71"]/div[1]/div/span[1]/span/span/span')))
botao_selecao_registrada.click()
time.sleep(3)
registrada = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ComboBox_73_listbox"]/li[2]')))
registrada.click()
time.sleep(10)

# Inicia o contador_dias 
contador_dias = 1

# Inicia o contador_arquivos
contador_arquivos=1

# Inicia o contador (data de início = data de hoje - 60 dias)
contador_data_start = -60

# Cria a data de start
data_hoje = datetime.today().date()
data_start = data_hoje + timedelta(days=contador_data_start)

# Definindo a variável que recebe o XPATH da mensagem de download em segundo plano
mensagem_segundo_plano = (By.XPATH, '//*[@id="1075"]/span') 

# Definindo a variável que recebe o XPATH da mensagem de download em segundo plano
botao_gerar_relatorio = (By.ID, 'button_10')

# Função para verificar se a mensagem está na tela
def botao_clicavel(botao_gerar_relatorio):
    try:
        navegador.wait.until(EC.element_to_be_clickable(*botao_gerar_relatorio))
        return True
    except:
        return False

# Função para verificar se a mensagem está na tela
def mensagem_download(mensagem_segundo_plano):
    try:
        navegador.find_element(*mensagem_segundo_plano)
        return True
    except:
        return False

# Pega o período dos últimos 60 dias e baixa os arquivos no intervalo de 2 em 2
while contador_dias <= 60:
    data_inicio = data_start + timedelta(days=contador_dias - 1)
    data_final = data_start + timedelta(days=contador_dias)
    data_inicio_str = data_inicio.strftime('%d/%m/%Y') + " 00:01"
    data_final_str = data_final.strftime('%d/%m/%Y') + " 23:59"

    input_data_inicio = wait.until(EC.visibility_of_element_located((By.ID, 'DateTimePicker_76')))
    input_data_inicio.clear()
    input_data_inicio.send_keys(data_inicio_str)

    input_data_final = wait.until(EC.visibility_of_element_located((By.ID, 'DateTimePicker_78')))
    input_data_final.clear()
    input_data_final.send_keys(data_final_str)

    print(f"Data 1={data_inicio_str}")
    print(f"Data 2={data_final_str}")
    print(f"Arquivo N°:{contador_arquivos}")
    print("-" * 100)

    time.sleep(4)

    #gerar_relatorio = wait.until(EC.visibility_of_element_located((By.ID, 'button_10')))

    while botao_clicavel(botao_gerar_relatorio):
        pass

    gerar_relatorio = wait.until(EC.element_to_be_clickable((By.ID, 'button_10')))
    gerar_relatorio.click()

    # Esperar indefinidamente até que a mensagem desapareça
    print(f"Arquivo N°:{contador_arquivos} Clicado Para Baixar")
    print("-" * 100)

    time.sleep(4)

    while mensagem_download(mensagem_segundo_plano):
        pass

    print(f"Mensagem sumiu")
    print("-" * 100)

    contador_arquivos+=1

    contador_dias = contador_dias + 2

time.sleep(10)

while mensagem_download(mensagem_segundo_plano):
    pass

print(f"Ultimo Arquivo Baixado")
print("-" * 100)

#########################################################################################################################################

def contar_arquivos(pasta):
    try:
        return len([arquivo for arquivo in os.listdir(pasta) if os.path.isfile(os.path.join(pasta, arquivo))])
    except FileNotFoundError:
        print("A pasta especificada não foi encontrada.")
        return 0

teste = 1

while True:
    quantidade_arquivos = contar_arquivos(caminho_completo)
    print(teste)
    print(f"Quantidade de arquivos na pasta: {quantidade_arquivos}")
    print("-" * 100)

    if quantidade_arquivos == 30:
        print("Atingiu 30 arquivos. Saindo do loop.")
        print("-" * 100)
        break

    teste += 1
    time.sleep(5)  # Aguarda 5 segundos antes de verificar novamente

#########################################################################################################################################

#Sair do Mylims
icone_logout = wait.until(EC.visibility_of_element_located((By.ID, 'Logout')))
icone_logout.click()

time.sleep(8)


'''
def gerar_novos_nomes(qtd_arquivos):
    data_start = datetime.now() - timedelta(days=60)  
    contador_dias = 1
    periodos = []

    # Pega o período dos últimos 60 dias e gera os nomes do arquivos no intervalo de 2 em 2 dias
    for arquivo in range(1, qtd_arquivos + 1):

        data_inicio = data_start + timedelta(days=contador_dias - 1)
        data_final = data_start + timedelta(days=contador_dias)
        data_inicio_str = data_inicio.strftime('%d-%m-%Y') + " 00-01"
        data_final_str = data_final.strftime('%d-%m-%Y') + " 23-59"

        periodo = f"({arquivo}) {data_inicio_str} - {data_final_str}.xlsx"
        periodos.append(periodo)

        contador_dias += 2

    #Retorna a lista para inserir os nomes nos arquivos respectivos
    return periodos

def renomear_arquivos(caminho_completo):
    arquivos = os.listdir(caminho_completo)
    qtd_arquivos = len(arquivos)
    novos_nomes = gerar_novos_nomes(qtd_arquivos)

    #Para cada arquivo na pasta ele aplica 1 item da lista 
    for arquivo, novo_nome in zip(arquivos, novos_nomes):
        caminho_antigo = os.path.join(caminho_completo, arquivo)
        caminho_novo = os.path.join(caminho_completo, novo_nome)
    
        os.rename(caminho_antigo, caminho_novo)
        print(f'{arquivo} RENOMEADO PARA: {novo_nome}')
    
    print("-" * 100)
    print("Finalizado")
    print("-" * 100)

renomear_arquivos(caminho_completo)'''


"""
# Aguarda indefinidamente para manter a janela aberta
try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    # Fecha o navegador ao interromper o script com Ctrl+C
    navegador.quit()
"""