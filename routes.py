from keep import app
from flask import render_template, session, request, flash, redirect, url_for

from models import Usuario

app.config['SECRET_KEY'] = 'df&kG73j@8s#koOW$'

user1 = Usuario('lucas', '12345')
user2 = Usuario('odin', '123')
user3 = Usuario('kayn', '321')

usuarios = {user1.username: user1.senha, 
            user2.username: user2.senha,
            user3.username: user3.senha}

@app.route('/')
def index():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))
    return render_template('index.html', titulo='Home')

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima, titulo='Login')

@app.route('/autenticar', methods=['POST', ])
def autenticar():
    usuario = request.form['usuario']
    if usuario in usuarios:
        if request.form['senha'] == usuarios[usuario]:
            session['usuario_logado'] = usuario
            flash(f'{usuario} logou com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
        else:
            flash('Senha incorreta, tente novamente.')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
    else:
        flash('Não logado, tente novamente!')
        return redirect(url_for('login'))

@app.route('/logout', methods=['POST', ])
def logout():
    session['usuario_logado'] = None
    flash('Sessão encerrada!')
    return redirect(url_for('login'))

