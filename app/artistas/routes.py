from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

from ..funciones import leeFichero, escribeFichero

artistasBP = Blueprint('artistas', __name__)

@artistasBP.get('/')
def getArtistas():
    artistas = leeFichero('app/ficheros/artistas.json')
    return jsonify(artistas)

@artistasBP.get("/<int:id>/canciones")
@jwt_required()
def getCancionesByArtist(id):
    artistas = leeFichero('app/ficheros/artistas.json')
    canciones = leeFichero('app/ficheros/canciones.json')

    list = []

    for cancion in canciones:
        if cancion['artista_id'] == id:
            list.append(cancion)


    if len(list) > 0:
        return list, 200
    else:
        return {'error': 'no hay canciones para ese artista'}