from datetime import datetime

from sqlalchemy import (
    Column,
    String,
    DateTime
)

from .meta import Base


class ProgrammingLanguage(Base):
    __tablename__ = 'languages'

    id = Column(String, primary_key=True)
    created_date = Column(DateTime, default=datetime.now, index=True)
    description = Column(String)