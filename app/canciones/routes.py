from flask import Blueprint, jsonify
from ..funciones import leeFichero, escribeFichero

cancionesBP = Blueprint('canciones', __name__)

@cancionesBP.get('/')
def getCanciones():
    canciones = leeFichero('app/ficheros/canciones.json')
    return jsonify(canciones)

@cancionesBP.get('/<int:id>')
def getCancionesByArtist(id):
    canciones = leeFichero('app/ficheros/canciones.json')
    list = []
    for cancion in canciones:
        if cancion['artista_id'] == id:
            list.append(cancion)

    if len(list) > 0:
        return list, 200
    else:
        return {'error': 'No se ha encontrado ninguna canción con ese id de artista'}