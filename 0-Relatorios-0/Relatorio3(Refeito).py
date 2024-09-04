import os
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
from twilio.rest import Client

def criar_pasta(caminho_base):

    # Obter a data de hoje no formato 'YYYY-MM-DD'
    data = datetime.today().strftime('%d-%m-%Y')
    # Combinar o caminho base com a data de hoje para formar o caminho completo do diretório do dia
    pasta_data = os.path.join(caminho_base, data)

    # Verificar se a pasta do dia já existe, se não, criar
    if not os.path.exists(pasta_data):
        os.makedirs(pasta_data)

    # Obter o horário atual no formato 'HH.MM'
    horario = datetime.today().strftime('%Hh%Mmin')
    # Definir o nome da nova pasta a ser criada dentro da pasta do dia
    pasta_horario = f"Relátorio_03_{horario}"

    # Combinar o caminho da pasta do dia com o nome da nova pasta
    caminho_final = os.path.join(pasta_data, pasta_horario)

    # Criar a nova pasta
    os.makedirs(caminho_final)

    return caminho_final

def iniciar_navegador(caminho_completo, url_labsoft):
    # Inicia o serviço do ChromeDriverManager e instala a versão mais recente
    servico = Service(ChromeDriverManager().install())

    # Configurações do Google Chrome
    opcoes_chrome = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": caminho_completo,  # Define o diretório de download padrão
        "download.prompt_for_download": False,  # Desativa o prompt de confirmação de download
        "directory_upgrade": True,  # Atualiza o diretório de download automaticamente
        "safebrowsing.enabled": True,  # Ativa o Safe Browsing
        "profile.default_content_settings.popups": 0,  # Desativa os popups
        "profile.default_content_setting_values.automatic_downloads": 1  # Permite downloads automáticos
    }

    # Configura as opções do Google Chrome
    opcoes_chrome.add_experimental_option("prefs", prefs)

    # Não abre habilita o Chorme abrir em janela
    #opcoes_chrome.add_argument('headless')

    # Inicializa o navegador com as opções configuradas
    navegador = webdriver.Chrome(service=servico, options=opcoes_chrome)

    # Abre e minimiza o navegador
    #navegador.minimize_window()

    # Abre e maximiza o navegador
    navegador.maximize_window()

    # Acessa o site especificado
    navegador.get(url_labsoft)

    # Adiciona um tempo de espera para garantir que a página carregue completamente
    tempo_espera = 30  # Tempo de espera em segundos
    espera = WebDriverWait(navegador, tempo_espera)

    # Retorna o navegador e a variável de espera como uma tupla
    return navegador, espera

def login(usuario,senha,espera):
    campo_login = espera.until(EC.visibility_of_element_located((By.ID, "Username")))
    campo_login.send_keys(usuario)
    campo_senha = espera.until(EC.visibility_of_element_located((By.ID, "Password")))
    campo_senha.send_keys(senha)  
    got_it = espera.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/a')))
    got_it.click()
    botao_login = espera.until(EC.visibility_of_element_located((By.CLASS_NAME, "labsoft-login-button-primary")))
    botao_login.click()

def dados_relatorio(espera):
    # Acessa a aba "Relatórios Gerenciais"
    relatorios_gerenciais = espera.until(EC.visibility_of_element_located((By.ID, "sectionitem_15")))
    relatorios_gerenciais.click()
    time.sleep(10)
    relatorios_gerenciais = espera.until(EC.visibility_of_element_located((By.ID, "sectionitem_15")))
    relatorios_gerenciais.click()
    time.sleep(10)
    #Seleção de Amostras
    botao_selecao_amostras = espera.until(EC.visibility_of_element_located((By.CLASS_NAME, "k-select")))
    botao_selecao_amostras.click()
    time.sleep(3)
    #Seleção Amostras - Métodos de Análises
    amostras_metodos_analises = espera.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ComboBox_47_listbox"]/li[15]')))
    amostras_metodos_analises.click()
    time.sleep(3)
    #Adicionar Situação Recebia
    botao_adicionar = espera.until(EC.visibility_of_element_located((By.ID, "button_70")))
    botao_adicionar.click()
    time.sleep(3)
    recebida = espera.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="Grid_127_noteditable"]/div[2]/table/tbody/tr[2]/td[2]')))
    recebida.click()
    time.sleep(3)
    botao_selecionar = espera.until(EC.visibility_of_element_located((By.ID, "button_122")))
    botao_selecionar.click()
    time.sleep(3)
    #Adicionar Situação em Analise
    botao_adicionar = espera.until(EC.visibility_of_element_located((By.ID, "button_70")))
    botao_adicionar.click()
    time.sleep(3)
    analise = espera.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="Grid_146_noteditable"]/div[2]/table/tbody/tr[3]/td[2]')))
    analise.click()
    time.sleep(3)
    botao_selecionar = espera.until(EC.visibility_of_element_located((By.ID, "button_141")))
    botao_selecionar.click()
    time.sleep(3)

def extrair_relatorio(navegador, espera, mensagem_segundo_plano):

    time.sleep(3)
    gerar_relatorio = espera.until(EC.visibility_of_element_located((By.ID, 'button_10')))
    gerar_relatorio.click()
    time.sleep(0.5)

    # Chame a função para monitorar mudanças no botão com ID 'button_10'
    while monitorar_mudanca_html(navegador, 'button_10',mensagem_segundo_plano):
        pass

    time.sleep(10)
    #Sair do Mylims
    icone_logout = espera.until(EC.visibility_of_element_located((By.ID, 'Logout')))
    icone_logout.click()
    time.sleep(10)

def mensagem_download(driver, mensagem_segundo_plano):
    try:
        driver.find_element(*mensagem_segundo_plano)
        return True
    except:
        return False
    
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
        # Verifique se "disabled" está presente no HTML do botão
        if '"disabled"' in html_atual:
            print("Botão ainda está desabilitado, continuando a monitorar...")
            time.sleep(10)  # Pequeno delay para não sobrecarregar o sistema
            continue  # Retorna ao início do loop para verificar novamente
        else:
            print("Botão habilitado, saindo do loop!")
            break  # Interrompe o loop quando o botão estiver habilitado

def main():
    url_labsoft = "https://labsoft-identitycenter-sts-prd.azurewebsites.net/Account/Login?ReturnUrl=%2Fconnect%2Fauthorize%2Fcallback%3Fclient_id%3DmyLIMSweb_JQuery%26redirect_uri%3Dhttps%253A%252F%252Foperator.mylimsweb.cloud%252Fcallback%252Findex%26response_type%3Dcode%26scope%3Dopenid%2520myLIMSweb_API_Create%2520myLIMSweb_API_Read%2520myLIMSweb_API_Update%2520myLIMSweb_API_Delete%2520DataViewer_API_Create%2520DataViewer_API_Read%2520DataViewer_API_Update%2520DataViewer_API_Delete%2520DataFactory_API_Create%2520DataFactory_API_Read%2520DataFactory_API_Update%2520DataFactory_API_Delete%26state%3D5d6e82bc61304a539eb558e4d12338df%26code_challenge%3DWMs1aUezfwUM-blX862r9-qXVhy9vgeQDopd1JCvTZI%26code_challenge_method%3DS256%26response_mode%3Dquery%26requesterClient%3Doperator"
    caminho_base = r"C:\Users\henrique.canhadas\OneDrive - Servmar Ambientais\Documentos\Codigos\GitHub\Python\0-Relatorios-0\Teste"
    mensagem_segundo_plano = (By.ID, "1059")
    usuario = "tvillavas"
    senha = "Operator24"  

    try:
        caminho_completo = criar_pasta(caminho_base)
        navegador, espera = iniciar_navegador(caminho_completo, url_labsoft)      

        login(usuario, senha, espera)
        dados_relatorio(espera)
        extrair_relatorio(navegador, espera, mensagem_segundo_plano)
        
        time.sleep(10)
    
    except Exception as e:
        # Envia SMS em caso de erro
        account_sid = 'AC906fb314ba2d4000b78916ef36dab13d'
        auth_token = 'd61f751b0989db1e918488c18a273d7e'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
          from_='+19133694026',
          body=f'Erro no Código: {str(e)}. POR FAVOR VERIFICAR.',
          to='+5511932738996'
        )

        print(message.sid)
    
if __name__ == "__main__":
    main()