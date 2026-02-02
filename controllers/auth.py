from flask import Blueprint, render_template, request, redirect, url_for
from models.usuario import Usuario, db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')

        novo_usuario = Usuario(nome=nome, email=email, senha=senha)
        
        try:
            db.session.add(novo_usuario)
            db.session.commit()
            return redirect(url_for('auth.login'))
        except Exception as e:
            db.session.rollback()
            return f"Erro ao cadastrar: {e}"

    return render_template('cadastro.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return render_template('dashboard.html')
    return render_template('login.html')