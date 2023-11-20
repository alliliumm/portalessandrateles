"""
Este módulo executa a aplicação Flask para o projeto.
Inclui rotas para renderizar a página inicial e enviar e-mails.

Vercel permite apenas um arquivo de execução de servidor no projeto.

Logo, futuras funcionalidades deverão ser adicionadas na pasta 'test'
para poder implantar no arquivo principal 'app.py'.
"""

from flask import Flask, render_template, request, jsonify
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os # Buscar no sistema operacional

# Utilizar o Flask neste arquivo, no caso: appy.py
app = Flask(__name__)

# Criptografar transições externas
app.secret_key = 'ABCabc123#'

# Rota inicial, com o nome que quiser
# Toda rota é seguida de função, esta será a renderização.
@app.route('/')
def index():
    return render_template('index.html')

# Envio de e-mail
@app.route('/send', methods=['GET', 'POST'])
def send():
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

            corpo_email = '''
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

    if(request.method == 'POST'):
        formContato = Contato(
            request.form["nome"],
            request.form["email"],
            request.form["assunto"],
            request.form["mensagem"]
        )

        resultado = enviar_email(formContato)

        mensagem = resultado['mensagem']
        sucesso = resultado['sucesso']
    else:
        mensagem = "Erro ao enviar o e-mail: Não foi possível concluir sua requisição."
        sucesso = False

        return jsonify(message=mensagem, success=sucesso)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)