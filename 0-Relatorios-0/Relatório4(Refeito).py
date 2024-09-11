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
    pasta_horario = f"Relátorio_04_{horario}"

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
    opcoes_chrome.add_argument('headless')

    # Inicializa o navegador com as opções configuradas
    navegador = webdriver.Chrome(service=servico, options=opcoes_chrome)

    # Abre e minimiza o navegador
    #navegador.minimize_window()

    # Abre e maximiza o navegador
    #navegador.maximize_window()

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

    #Seleção Amostras (drop-list) 
    amostras = espera.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ComboBox_47_listbox"]/li[2]')))
    amostras.click()
    time.sleep(3)

    #Situação da Amostra - Histórico
    situação_amostra = espera.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="layoutrow_71"]/div[1]/div/span[1]/span/span'))) 
    situação_amostra.click()
    time.sleep(3)

    #Recebida
    situação_recebida = espera.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ComboBox_73_listbox"]/li[3]'))) 
    situação_recebida.click()
    time.sleep(3)

def extrair_relatorio(navegador, espera, mensagem_segundo_plano, num_periodos=12, dias_periodo=30):
    # Data atual do sistema
    data_atual = datetime.now()

    # Lista para armazenar os períodos
    periodos = []

    # Gerando os períodos de 30 dias diretamente no loop
    for _ in range(num_periodos):
        data_final = data_atual
        data_atual -= timedelta(days=dias_periodo)
        periodos.append((data_atual.strftime('%d/%m/%Y'), data_final.strftime('%d/%m/%Y')))

    for contador_arquivos, (data_inicio_str, data_final_str) in enumerate(periodos, start=1):
        print(f"Geração {contador_arquivos}º período")
        print(f"{contador_arquivos}º período = Inicio:{data_inicio_str} 00:01")
        print(f"{contador_arquivos}º período = Final:{data_final_str} 23:59")
        
        # Inserindo as datas no sistema
        input_data_inicio = espera.until(EC.visibility_of_element_located((By.ID, 'DateTimePicker_76')))
        input_data_inicio.clear()
        input_data_inicio.send_keys(f"{data_inicio_str} 00:01")

        input_data_final = espera.until(EC.visibility_of_element_located((By.ID, 'DateTimePicker_78')))
        input_data_final.clear()
        input_data_final.send_keys(f"{data_final_str} 23:59")

        # Clicar em Gerar Relatório
        gerar_relatorio = espera.until(EC.visibility_of_element_located((By.ID, 'button_10')))
        gerar_relatorio.click()
        time.sleep(0.5)
        
        while monitorar_mudanca_html(navegador, 'button_10', mensagem_segundo_plano):
            pass

        print(f"Arquivo N°:{contador_arquivos} Clicado Para Baixar")
        print("-" * 100)

    time.sleep(10)
    icone_logout = espera.until(EC.visibility_of_element_located((By.ID, 'Logout')))
    icone_logout.click()
    time.sleep(10)

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
                <h2><strong>Relatório 4</strong> - Erro no Código</h2>
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
    if quantidade_arquivos < 12:
        assunto = "🚨 Menos de 12 arquivos na pasta"
        mensagem = f"Há apenas <strong>{quantidade_arquivos}</strong> arquivos no <strong>Relatório 4</strong> na pasta: <p>{caminho_completo}</p>"

    elif quantidade_arquivos > 12:
        assunto = "🚨 Mais de 12 arquivos na pasta"
        mensagem = f"Há <strong>{quantidade_arquivos}</strong> arquivos no <strong>Relatório 4</strong> na pasta: <p>{caminho_completo}</p>"

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
    mensagem_segundo_plano = (By.ID, "1042")
    usuario = "tvillavas"
    senha = "Operator24"  

    try:
        caminho_completo = criar_pasta(caminho_base)
        navegador, espera = iniciar_navegador(caminho_completo, url_labsoft)      

        login(usuario, senha, espera)
        dados_relatorio(espera)
        extrair_relatorio(navegador, espera, mensagem_segundo_plano)
        
        email_quantidade(caminho_completo)
        
        time.sleep(10)
    
    except Exception as e:
        email_erro(e)
        print("E-mail de erro enviado com sucesso.")
       
if __name__ == "__main__":
    main()