from wsgiref.util import request_uri

import bcrypt
from flask import Blueprint, request
from flask_jwt_extended import create_access_token

from app.funciones import leeFichero, escribeFichero

usuariosBP = Blueprint('usuarios', __name__)

@usuariosBP.post('/')
def addUser():
    users = leeFichero('app/ficheros/usuarios.json')

    if request.is_json:
        user = request.get_json()
        password = user['password'].encode('utf-8')

        #generamos la salt
        salt = bcrypt.gensalt()

        #calculamos el hash y lo convertimos en hexadecimal
        hash = bcrypt.hashpw(password, salt).hex()

        user['password'] = hash

        users.append(user)

        escribeFichero(users, 'app/ficheros/usuarios.json')

        #creamos el token
        token = create_access_token(identity=user['username'])
        return {'token': token}, 201
    return {'error': 'error'}, 415

@usuariosBP.post('/login')
def login():
    users = leeFichero('app/ficheros/usuarios.json')

    if request.is_json:
        user = request.get_json()

        username = user['username']
        password = user['password'].encode('utf-8')

        for userFile in users:
            if userFile['username'] == username:
                passwordFile = userFile['password']

                if bcrypt.checkpw(password, bytes.fromhex(passwordFile)):
                    token = create_access_token(identity=username)

                    return {'token': token}, 200
                else:
                    return {'error': 'No autorizado'}, 401

        return {'error': 'user not found'}, 404
    return {'error': 'request must be a json'}, 415
