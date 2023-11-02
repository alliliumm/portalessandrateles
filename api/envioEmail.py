import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from api.autenticacao import obter_token_acesso

# Colocar as configurações no app

class Contato:
    def __init__(self, nome, email, assunto, mensagem):
        self.nome = nome
        self.email = email
        self.assunto = assunto
        self.mensagem = mensagem

# Envio de e-mail
def enviar_email(formContato):

    # Configurar o servidor SMTP do Google
    servidor_smtp = smtplib.SMTP(
        'smtp.gmail.com', 
        587
    )
    servidor_smtp.starttls()

    token_acesso = obter_token_acesso()  # Obtenha o token de acesso

    servidor_smtp.login(token_acesso, None)  # Autentique com o token de acesso

    # Personalizar o e-mail
    assunto = f'Nova mensagem de {formContato.nome} - Assunto: {formContato.assunto}'
    remetente = 'contalessandrateles@gmail.com'
    destinatario = [
        'alessandrateles911@gmail.com', 
        'contalessandrateles@gmail.com'
    ]
    corpo_email = f'''
        {formContato.nome} com o e-mail {formContato.email} enviou a seguinte mensagem:
        Assunto: {formContato.assunto}
        Mensagem: {formContato.mensagem}
    '''

    # Enviar e-mail
    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = ', '.join(destinatario)
    msg['Subject'] = assunto
    msg.attach(MIMEText(corpo_email, 'plain'))

    # Enviar o e-mail
    servidor_smtp.sendmail(remetente, destinatario, msg.as_string())

    # Fechar a conexão com o servidor SMTP
    servidor_smtp.quit()