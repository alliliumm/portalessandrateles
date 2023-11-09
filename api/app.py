from flask import Flask, render_template, redirect, request, jsonify
from envioEmail import enviar_email, Contato

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
        
        return jsonify(message=resultado['mensagem'], success=resultado['sucesso'])

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)