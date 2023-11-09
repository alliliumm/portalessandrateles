import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os # Buscar no sistema operacional

# Colocar as configurações no app
class Contato:
    def __init__(self, nome, email, assunto, mensagem):
        self.nome = nome
        self.email = email
        self.assunto = assunto
        self.mensagem = mensagem

# Envio de e-mail
def enviar_email(formContato):
    mail_settings = {
        "MAIL_SERVER": "smtp.gmail.com",
        "MAIL_PORT": 587,
        "MAIL_USE_TLS": True,
        "MAIL_USE_SSL": False,
        "MAIL_USERNAME": os.environ.get("EMAIL"),
        "MAIL_PASSWORD": os.environ.get("SENHA")   
    }

    try: # Tentar Enviar o E-mail

        # Configurar o servidor SMTP do Google
        servidor_smtp = smtplib.SMTP(mail_settings['MAIL_SERVER'], mail_settings['MAIL_PORT'])
        servidor_smtp.starttls()

        servidor_smtp.login(mail_settings['MAIL_USERNAME'], mail_settings['MAIL_PASSWORD'])  # Autentique com o token de acesso

        # Personalizar o e-mail
        assunto = f'{formContato.assunto} - {formContato.nome}'
        remetente = 'contalessandrateles@gmail.com'
        destinatario = [
            # 'alessandrateles911@gmail.com', 
            'contalessandrateles@gmail.com'
        ]
        header_email = f'''
            <h3>{formContato.nome} com o e-mail {formContato.email} enviou a seguinte mensagem:</h3> 
        '''

        # Enviar e-mail
        msg = MIMEMultipart()
        msg['From'] = remetente
        msg['To'] = ', '.join(destinatario)
        msg['Subject'] = assunto

        # Com HTML definindo cabeçalho
        parte_html = MIMEText(header_email, 'html')
        msg.attach(parte_html)

        # De acordo com a formatação do usuário em texto simples
        parte_texto = MIMEText(formContato.mensagem, 'plain')
        msg.attach(parte_texto)

        servidor_smtp.sendmail(remetente, destinatario, msg.as_string())

        corpo_email = f'''
            <p>Vamos lá</p>
        '''

        msg = MIMEMultipart()
        msg['From'] = remetente
        msg['To'] = formContato.email
        msg['Subject'] = 'Agradeço o seu contato! - Alessandra Teles'
        msg.attach(MIMEText(corpo_email, 'html'))

        servidor_smtp.sendmail(remetente, formContato.email, msg.as_string())

        resultado = {"sucesso": True, "mensagem": "E-mail enviado com sucesso!"}
    except Exception as e:
        if not mensage:
            erro = str(e)
            mensage = "Erro ao enviar o e-mail: " + erro
        resultado = {"sucesso": False, "mensagem": mensage}

    # Fechar a conexão com o servidor SMTP
    servidor_smtp.quit()

    return resultado