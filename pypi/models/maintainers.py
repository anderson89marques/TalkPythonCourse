from datetime import datetime

from sqlalchemy import (
    Column,
    String,
    Integer
)

from .meta import Base


class Mantainer(Base):
    __tablename__ = 'maintainers'

    user_id = Column(Integer, primary_key=True)
    package_id = Column(String, primary_key=True)