from datetime import datetime

import bcrypt

from sqlalchemy import (
    Column,
    String,
    Integer,
    DateTime
)

from .meta import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=True)
    email = Column(String, index=True, nullable=True)
    hashed_password = Column(String, index=True, nullable=True)
    created_date = Column(DateTime, default=datetime.now, index=True)
    profile_image_url = Column(String)
    last_login = Column(DateTime, default=datetime.now, index=True)

    def set_password(self, pw):
        pwhash = bcrypt.hashpw(pw.encode('utf8'), bcrypt.gensalt())
        self.hashed_password =  pwhash.decode('utf8')

    def check_password(self, pw):
        if self.hashed_password is not None:
            expected_hash = self.hashed_password.encode('utf8')
            return bcrypt.checkpw(pw.encode('utf8'), expected_hash)
        return False