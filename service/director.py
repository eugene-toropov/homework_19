from dao.director import DirectorDAO


class DirectorService:
    """
    Класс сервис для сущности Director.
    В поля класса добавляем объект ДАО.
    """
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_one(self, bid):
        """
        Метод для получения режиссера по его id через обращение к ДАО.
        """
        return self.dao.get_one(bid)

    def get_all(self):
        """
        Метод для получения списка всех режиссеров через обращение к ДАО.
        """
        return self.dao.get_all()

    def create(self, director_d):
        """
        Метод для создания нового режиссера через обращение к ДАО.
        """
        return self.dao.create(director_d)

    def update(self, director_d):
        """
        Метод для обновления экземпляра класса режиссер через обращение к ДАО.
        """
        self.dao.update(director_d)
        return self.dao

    def delete(self, rid):
        """
        Метод для удаления экземпляра класса режиссер по его id через обращение к ДАО.
        """
        self.dao.delete(rid)
