from pypi.models import User

def user_count(dbsession) -> int:
    return dbsession.query(User).count()

def create_user(dbsession, name: str, email: str, password: str) ->  User:
    user = User()
    user.name = name
    user.email = email
    user.set_password(password)

    dbsession.add(user)

    return user

def login_user(dbsession, email, password):
    user: User = dbsession.query(User).filter(User.email == email).first()

    if not user or not user.check_password(password):
        return None

    return user