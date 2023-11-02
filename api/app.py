from flask import Flask, render_template, redirect, request, jsonify
# from flask_mail import Mail, Message
from envioEmail import enviar_email, Contato
import os # Buscar no sistema operacional
# Importações necessárias de ferramentas

# Utilizar o Flask neste arquivo, no caso: appy.py
app = Flask(__name__)

# Criptografar transições externas
app.secret_key = 'ABCabc123#'

#------------------------------------------------------------------------------
# mail_settings = {
#     "MAIL_SERVER": "smtp.gmail.com",
#     "MAIL_PORT": 465,
#     "MAIL_USE_TLS": False,
#     "MAIL_USE_SSL": True,
#     "MAIL_USERNAME": os.environ.get("EMAIL"),
#     "MAIL_PASSWORD": os.environ.get("SENHA")   
# }

# app.config.update(mail_settings)
# # Colocar as configurações no app

# mail = Mail(app)
#------------------------------------------------------------------------------

# Rota inicial, com o nome que quiser
# Toda rota é seguida de função, esta será a renderização.
@app.route('/')
def index():
    return render_template('index.html')

# Envio de e-mail
@app.route('/send', methods=['GET', 'POST'])
def send():
    if(request.method == 'POST'):
        formContato = Contato(
            request.form["nome"],
            request.form["email"],
            request.form["assunto"],
            request.form["mensagem"]
        )

        enviar_email(formContato)

        # Mensagem enviada com sucesso!
        success_message = 'Ainda sendo implementado.'
        error_message = 'Erro ao enviar o formulário. Por favor, tente novamente mais tarde.'
        
    if(request.method == 'POST'): #condicao para saber se foi ou nao 
        return jsonify(message=success_message, success=True)
    else:
        return jsonify(message=error_message, success=False)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=False)