from app.model import User
from app.form import UserForm


class UserService:
    @classmethod
    def create(cls) -> User:
        user = User()
        User.save(user)
        return user

    @classmethod
    def get(cls) -> User:
        return User.find_first()

    @classmethod
    def fill(cls, form: UserForm) -> None:
        user = cls.get()
        form.process(obj=user)
        return user

    @classmethod
    def update(cls, form: UserForm) -> User:
        user = cls.get()
        form.populate_obj(user)
        User.save(user)
        return user
