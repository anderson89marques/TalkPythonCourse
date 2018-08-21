from datetime import datetime

from sqlalchemy import (
    Column,
    BigInteger,
    String,
    DateTime
)

from .meta import Base


class Download(Base):
    __tablename__ = 'downloads'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    created_date = Column(DateTime, default=datetime.now, index=True)

    package_id = Column(String, index=True)
    release_id = Column(BigInteger, index=True)
    
    ip_address = Column(String)
    user_agent = Column(String)