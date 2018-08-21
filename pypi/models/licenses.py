from datetime import datetime

from sqlalchemy import (
    Column,
    String,
    DateTime
)

from .meta import Base


class License(Base):
    __tablename__ = 'licenses'

    id = Column(String, primary_key=True)
    created_date = Column(DateTime, default=datetime.now, index=True)
    description = Column(String)