from flask import Flask
from flask_jwt_extended import JWTManager

from app.artistas.routes import artistasBP
from app.canciones.routes import cancionesBP
from app.usuarios.routes import usuariosBP

app = Flask(__name__)
app.config['SECRET_KEY'] = 'miclave'

jwt = JWTManager(app)

app.register_blueprint(cancionesBP, url_prefix='/canciones')
app.register_blueprint(artistasBP, url_prefix='/artistas')
app.register_blueprint(usuariosBP, url_prefix='/usuarios')