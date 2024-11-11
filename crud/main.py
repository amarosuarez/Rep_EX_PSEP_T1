from token import FSTRING_END

import requests


def login():

    token = ''
    resultado = ''
    log = False

    while not log:
        username = input('username: ')
        password = input('password: ')

        resultado = requests.post(
            "http://localhost:5050/usuarios/login",
            json={"username": username, "password": password},
            headers={"Content-Type": "application/json"})

        if resultado:
            log = True
        else:
            print('error')

        token = resultado.json().get("token")
    return token


def main():
    token = login()
    print(token)


if __name__ == '__main__':
    main()