from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# App e suas Configurações
app = Flask(__name__)

# Vincula ao banco --------------
usuario_db = "root" ; senha_db = "123456" ; banco_db = "bank"
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{usuario_db}:{senha_db}@localhost:3306/{banco_db}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# formulário --------------
app.config['SECRET_KEY'] = 'nome-seguro-baby'
app.app_context().push()

db = SQLAlchemy(app)

# Flask-Login
lm = LoginManager()
lm.init_app(app)



