from flask import Flask, redirect, url_for
from models.usuario import db
from controllers.auth import auth_bp

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('auth.cadastro'))

# Configuração MySQL: usuario:senha@host/nome_do_banco
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/db_ICS'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa o banco com o app
db.init_app(app)

# Registra as rotas
app.register_blueprint(auth_bp)

# Cria as tabelas automaticamente
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)