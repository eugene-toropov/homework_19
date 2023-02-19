from dao.model.user import User


class UserDAO:
    """
    Класс ДАО для сущности User.
    В поля класса добавляем сессию подключения.
    """
    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        """
        Метод получения юзера по его id.
        """
        return self.session.query(User).get(uid)

    def get_all(self):
        """
        Метод получения списка всех пользователей.
        """
        return self.session.query(User).all()

    def get_by_name(self, name):
        """
        Метод получения пользователя по его имени.
        """
        return self.session.query(User).filter(User.username == name).first()

    def create(self, user_d):
        """
        Метод создания и добавления пользователя в список.
        """
        ent = User(**user_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, uid):
        """
        Метод удаления пользователя по его id.
        """
        user = self.get_one(uid)
        self.session.delete(user)
        self.session.commit()

    def update(self, user_d):
        """
        Метод обновления данных пользователя.
        """
        user = self.get_one(user_d.get("id"))

        user.name = user_d.get("name")
        user.role = user_d.get("role")

        self.session.add(user)
        self.session.commit()
