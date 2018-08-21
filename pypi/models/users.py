from datetime import datetime

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