"""
Este módulo executa a aplicação Flask para o projeto.
Inclui rotas para renderizar a página inicial e enviar e-mails.
"""

from flask import Flask, render_template, request, jsonify
from envio_email import enviar_email, Contato # Erro que não influencia em ambiente de teste local

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