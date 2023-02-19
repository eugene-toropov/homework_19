from marshmallow import Schema, fields

from setup_db import db


class User(db.Model):
    """
    Класс/модель ДБ 'User'.
    Прописываем поля класса: id, username, password, role.
    """
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)
    role = db.Column(db.String)


class UserSchema(Schema):
    """
    Схема сериализации/десериализации для класса 'User'.
    На основе полей класса 'User' создаем схему с указанием типа данных.
    """
    id = fields.Int()
    username = fields.Str()
    password = fields.Str()
    role = fields.Str()
