from flask import Flask, render_template, request, redirect, url_for
from flask_httpauth import HTTPBasicAuth
import sqlite3
import logging

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)
auth = HTTPBasicAuth()

# Define o caminho para o banco de dados
DB_PATH = 'plantao.db'

# Dicionário com os usuários e senhas
USERS = {
    "plantonista": "guarana"
}

# Função que verifica se um usuário está autorizado
@auth.verify_password
def verify(username, password):
    if not (username and password):
        return False
    return USERS.get(username) == password

@app.route('/plantao', methods=['GET', 'POST'])
@auth.login_required
def cadastro_plantonista():
    if request.method == 'POST':
        plantonista = request.form['plantonista']
        data = request.form['data']
        
        # Conecta ao banco de dados
        conn = sqlite3.connect(DB_PATH)
        
        # Insere os dados na tabela "plantao"
        cur = conn.cursor()
        cur.execute("INSERT INTO plantao (plantonista, data) VALUES (?, ?)", (plantonista, data))
        conn.commit()
        
        # Fecha a conexão com o banco de dados
        conn.close()
        
        # Redireciona para a página de confirmação
        return redirect(url_for('cadastro_sucesso', plantonista=plantonista, data=data))
    
    return render_template('index.html')

@app.route('/cadastro_sucesso')
def cadastro_sucesso():
    plantonista = request.args.get('plantonista')
    data = request.args.get('data')
    return render_template('cadastro_sucesso.html', plantonista=plantonista, data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=5000)