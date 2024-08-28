# portfolio
Portfólio Responsivo com Bootstrap e Flask

Necessário o Python instalado junto com as suas extensões no VSCode e instalar pelo terminal, recomendável no local do projeto, a biblioteca do Flask através do comando:

pip install flask
<!-- pip install Flask-Mail -->
pip freeze > requirements.txt
pip list -v 

Subir o servidor Python apenas executando o arquivo app.py com extensão Code Runner do VsCode ou executando pelo terminal na chamada do arquivo.

python api/app.py

Para funcionamento de envio de e-mails pelo Gmail, é necessário ativar Verificação de Etapas da sua conta Google a qual enviará os e-mails, em seguida definir Senha de App, sendo altenativa da sua senha atual ao se conectar com o servidor SMTP,logo será necessário criar o seu próprio arquivo "env" para definição de usuário e senha, tem-se o exemplo deste tipo de arquivo no diretório principal do projeto.