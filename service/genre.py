from dao.genre import GenreDAO


class GenreService:
    """
    Класс сервис для сущности Genre.
    В поля класса добавляем объект ДАО.
    """
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_one(self, bid):
        """
        Метод для получения жанра по его id через обращение к ДАО.
        """
        return self.dao.get_one(bid)

    def get_all(self):
        """
        Метод для получения списка всех жанров через обращение к ДАО.
        """
        return self.dao.get_all()

    def create(self, genre_d):
        """
        Метод для создания нового жанра через обращение к ДАО.
        """
        return self.dao.create(genre_d)

    def update(self, genre_d):
        """
        Метод для обновления экземпляра класса жанр через обращение к ДАО.
        """
        self.dao.update(genre_d)
        return self.dao

    def delete(self, rid):
        """
        Метод для удаления экземпляра класса жанр по его id через обращение к ДАО.
        """
        self.dao.delete(rid)
