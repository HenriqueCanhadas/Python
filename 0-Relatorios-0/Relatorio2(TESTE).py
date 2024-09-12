import os
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
import smtplib
import email.message

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
    pasta_horario = f"Relátorio_02_{horario}"

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
    
    #got_it = espera.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/a')))
    #got_it.click()
    
    botao_login = espera.until(EC.visibility_of_element_located((By.CLASS_NAME, "labsoft-login-button-primary")))
    botao_login.click()

def logout(navegador, espera):
    time.sleep(5)
    # Sair do Mylims usando clique via JavaScript
    icone_logout = espera.until(EC.presence_of_element_located((By.ID, 'Logout')))
    navegador.execute_script("arguments[0].click();", icone_logout)
    time.sleep(10)

def dados_relatorio(espera):
    relatorios_gerenciais = espera.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[data-test='Relatórios Gerenciais']")))
    relatorios_gerenciais.click()
    time.sleep(10)
    relatorios_gerenciais = espera.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[data-test='Relatórios Gerenciais']")))
    relatorios_gerenciais.click()
    time.sleep(10)
    botao_selecao_amostras = espera.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span.k-select")))
    botao_selecao_amostras.click()
    time.sleep(3)
    amostras_informacoes_analises = espera.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "li[data-offset-index='11']")))
    amostras_informacoes_analises.click()
    time.sleep(3)
    botao_selecao_registrada = espera.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span[aria-controls='ComboBox_72_listbox']")))
    botao_selecao_registrada.click()
    time.sleep(3)
    
    # Espera até que o elemento esteja visível
    registrada = espera.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ComboBox_72_listbox"]/li[2]')))

    # Clica no elemento
    registrada.click()

    time.sleep(3)

def extrair_relatorio(navegador, espera, mensagem_segundo_plano, usuario, senha):
    # Inicia o contador_dias 
    contador_dias = 1
    
    # Inicia o contador_arquivos
    contador_arquivos=1
    
    # Inicia o contador (data de início = data de hoje - 60 dias)
    contador_data_start = -60
    
    # Cria a data de start
    data_hoje = datetime.today().date()
    data_start = data_hoje + timedelta(days=contador_data_start)
        
    # Pega o período dos últimos 60 dias e baixa os arquivos no intervalo de 2 em 2
    while contador_dias <= 60:

        login(usuario,senha,espera)
        dados_relatorio(espera)

        data_inicio = data_start + timedelta(days=contador_dias - 1)
        data_final = data_start + timedelta(days=contador_dias)
        data_inicio_str = data_inicio.strftime('%d/%m/%Y') + " 00:01"
        data_final_str = data_final.strftime('%d/%m/%Y') + " 23:59"
    
        input_data_inicio = WebDriverWait(navegador, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[data-test='StartDate']")))
        input_data_inicio.clear()
        input_data_inicio.send_keys(data_inicio_str)
    
        input_data_final = WebDriverWait(navegador, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[data-test='EndDate']")))
        input_data_final.clear()
        input_data_final.send_keys(data_final_str)
    
        print(f"Data 1={data_inicio_str}")
        print(f"Data 2={data_final_str}")
        print(f"Arquivo N°:{contador_arquivos}")
    
        gerar_relatorio = espera.until(EC.visibility_of_element_located((By.ID, 'button_10')))
        gerar_relatorio.click()
        # Esperar indefinidamente até que a mensagem desapareça
        print(f"Arquivo N°:{contador_arquivos} Clicado Para Baixar")
        time.sleep(0.5)
        
        # Chame a função para monitorar mudanças no botão com ID 'button_10'
        while monitorar_mudanca_html(navegador, 'button_10',mensagem_segundo_plano):
            pass
        
        contador_arquivos+=1
    
        contador_dias = contador_dias + 2

        logout(navegador,espera)
        
def mensagem_download(driver, mensagem_segundo_plano):
    try:
        driver.find_element(*mensagem_segundo_plano)
        return True
    except:
        time.sleep(10)
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

def email_erro(e):
        corpo_email = f"""
        <html>
            <body>
                <h2><strong>Relatório 2</strong> - Erro no Código</h2>
                <p><strong>Data e Hora:</strong> {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}</p>
                <p><strong>Descrição do Erro:</strong></p>
                <p style="color: red;"><pre>{str(e)}</pre></p>
            </body>
        </html>
        """

        # Configuração do e-mail
        msg = email.message.Message()
        msg['Subject'] = "🚨 Erro no Projeto Automação"
        msg['From'] = 'tiservmar@gmail.com'
        msg['To'] = 'vitor.lucas@servmarambiental.com'
        msg['Cc'] = 'henrique.canhadas@servmarambiental.com'  # Adicionando Cópia (Cc)
        password = 'vfbppqosrgajjgvx'

        # Configurando o corpo do e-mail
        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(corpo_email)

        # Lista de destinatários (inclui To e Cc)
        destinatarios = [msg['To']] + [msg['Cc']]

        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()
        servidor.login(msg['From'], password)
        servidor.sendmail(msg['From'], destinatarios, msg.as_string().encode('utf-8'))
        servidor.quit()

def email_quantidade(caminho_completo):
    # Contando o número de arquivos no diretório
    time.sleep(10)
    arquivos = os.listdir(caminho_completo)
    quantidade_arquivos = len([arquivo for arquivo in arquivos if os.path.isfile(os.path.join(caminho_completo, arquivo))])

    # Definir o assunto e a mensagem com base na quantidade de arquivos
    if quantidade_arquivos < 30:
        assunto = "🚨 Menos de 30 arquivos na pasta"
        mensagem = f"Há apenas <strong>{quantidade_arquivos}</strong> arquivos no <strong>Relatório 2</strong> na pasta: <p>{caminho_completo}</p>"

    elif quantidade_arquivos > 30:
        assunto = "🚨 Mais de 30 arquivos na pasta"
        mensagem = f"Há <strong>{quantidade_arquivos}</strong> arquivos no <strong>Relatório 2</strong> na pasta: <p>{caminho_completo}</p>"

    else:
        return
    
    # Corpo do e-mail HTML
    corpo_email = f"""
    <html>
        <body>
            <p><strong>Data e Hora:</strong> {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}</p>
            <p>{mensagem}</p>
        </body>
    </html>
    """
    # Configuração do e-mail
    msg = email.message.Message()
    msg['Subject'] = assunto
    msg['From'] = 'tiservmar@gmail.com'
    msg['To'] = 'vitor.lucas@servmarambiental.com'
    msg['Cc'] = 'henrique.canhadas@servmarambiental.com'  # Adicionando Cópia (Cc)
    password = 'vfbppqosrgajjgvx'  # A senha deve ser armazenada de forma segura!
    # Configurando o corpo do e-mail
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)
    # Lista de destinatários (inclui To e Cc)
    destinatarios = [msg['To']] + [msg['Cc']]
    # Enviando o e-mail
    servidor = smtplib.SMTP('smtp.gmail.com', 587)
    servidor.starttls()
    servidor.login(msg['From'], password)
    servidor.sendmail(msg['From'], destinatarios, msg.as_string().encode('utf-8'))
    servidor.quit()
    print("E-mail enviado com sucesso!")

def main():
    url_labsoft = "https://labsoft-identitycenter-sts-prd.azurewebsites.net/Account/Login?ReturnUrl=%2Fconnect%2Fauthorize%2Fcallback%3Fclient_id%3DmyLIMSweb_JQuery%26redirect_uri%3Dhttps%253A%252F%252Foperator.mylimsweb.cloud%252Fcallback%252Findex%26response_type%3Dcode%26scope%3Dopenid%2520myLIMSweb_API_Create%2520myLIMSweb_API_Read%2520myLIMSweb_API_Update%2520myLIMSweb_API_Delete%2520DataViewer_API_Create%2520DataViewer_API_Read%2520DataViewer_API_Update%2520DataViewer_API_Delete%2520DataFactory_API_Create%2520DataFactory_API_Read%2520DataFactory_API_Update%2520DataFactory_API_Delete%26state%3D5d6e82bc61304a539eb558e4d12338df%26code_challenge%3DWMs1aUezfwUM-blX862r9-qXVhy9vgeQDopd1JCvTZI%26code_challenge_method%3DS256%26response_mode%3Dquery%26requesterClient%3Doperator"
    caminho_base = r"C:\Users\henrique.canhadas\OneDrive - Servmar Ambientais\Documentos\Codigos\GitHub\Python\0-Relatorios-0\Teste"
    mensagem_segundo_plano = (By.ID, "1075")
    usuario = "tvillavas"
    senha = "Operator24"  

    try:
        caminho_completo = criar_pasta(caminho_base)
        navegador, espera = iniciar_navegador(caminho_completo, url_labsoft)      

        extrair_relatorio(navegador, espera, mensagem_segundo_plano, usuario, senha)

        email_quantidade(caminho_completo)
        
        time.sleep(10)
    
    except Exception as e:
        email_erro(e)
        print("E-mail de erro enviado com sucesso.")

if __name__ == "__main__":
    for _ in range(5):
        main()