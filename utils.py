import jwt
from flask import request, abort

from constants import JWT_ALGORITHM, JWT_SECRET


def auth_required(func):
    """
    Декоратор auth_required.

    Проверяет авторизован ли пользователь, если да - извлекает токен и декодирует его.
    Если все ок - возвращает выполняемую функцию. Если нет - останавливает выполнение.
    """
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)

        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]

        try:
            jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        except Exception as e:
            print('JWT Decode Exception', e)
            abort(401)

        return func(*args, **kwargs)

    return wrapper


def admin_required(func):
    """
    Декоратор admin_required.

    Проверяет авторизован ли пользователь, если да - извлекает токен и декодирует его.
    Так же проверяет роль пользователя.
    Если все ок - возвращает выполняемую функцию. Если нет - останавливает выполнение.
    """
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)

        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]

        try:
            user = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
            if user['role'] != 'admin':
                abort(401)
        except Exception as e:
            print('JWT Decode Exception', e)
            abort(401)

        return func(*args, **kwargs)

    return wrapper
