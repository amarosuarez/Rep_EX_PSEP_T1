import json


def leeFichero(ruta):
    archivo = open(ruta, 'r')
    data = json.load(archivo)
    archivo.close()
    return data

def escribeFichero(data, ruta):
    archivo = open(ruta, 'w')
    json.dump(data, archivo)
    archivo.close()