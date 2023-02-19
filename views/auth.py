from flask import request
from flask_restx import Resource, Namespace

from implemented import auth_service

auth_ns = Namespace('auth')


@auth_ns.route('/')
class AuthView(Resource):
    """
    Класс представления для аутентификации.
    """
    def post(self):
        """
        Метод post.

        Получает логин и пароль из Body запроса в виде JSON, далее проверяет соответствии с данными в БД
        (есть ли такой пользователь, такой ли у него пароль) и если всё оk — генерит пару access_token и
        refresh_token и отдает их в виде JSON.
        """
        data = request.json

        username = data.get('username')
        password = data.get('password')

        if None in [username, password]:
            return '', 400

        tokens = auth_service.generate_tokens(username, password)

        return tokens, 201

    def put(self):
        """
        Метод put.

        Получает refresh_token из Body запроса в виде JSON, далее проверяет refresh_token и
        если он не истек и валиден — генерит пару access_token и refresh_token и отдает их в виде JSON.
        """
        data = request.json
        token = data.get('refresh_token')

        tokens = auth_service.approve_refresh_token(token)

        return tokens, 201
