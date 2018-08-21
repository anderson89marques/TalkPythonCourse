from pypi.models import User

def user_count(dbsession) -> int:
    return dbsession.query(User).count()