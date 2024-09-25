import smtplib
import email.message


def enviar_email():
    corpo_email = """
    <p>1°O coringa enloqueceu por mt menos</p>
    <p>2°E o pix nada ainda!?</p>
    <p><strong>Erro no Código: {str(e)}. POR FAVOR VERIFICAR.</strong></p>
    """
    
    msg = email.message.Message()
    msg['Subject'] = "Rodou Rodou"
    msg['From'] = 'tiservmar@gmail.com'
    msg['To'] = 'vitor.lucas@servmarambiental.com'
    msg['Cc'] = 'henrique.canhadas@servmarambiental.com'  # Adicionando Cópia (Cc)
    password = 'vfbppqosrgajjgvx'

    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    breakpoint()

    # Lista de destinatários (inclui To e Cc)
    destinatarios = [msg['To']] + [msg['Cc']]

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], destinatarios, msg.as_string().encode('utf-8'))
    s.quit()

    print("Email Enviado")


enviar_email()