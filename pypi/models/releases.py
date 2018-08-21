from datetime import datetime

from sqlalchemy import (
    Column,
    String,
    BigInteger,
    Integer,
    DateTime,
    ForeignKey,
    orm
)

from .meta import Base


class Release(Base):
    __tablename__ = 'releases'

    id = Column(Integer, primary_key=True, autoincrement=True)
    major_ver = Column(BigInteger, index=True)
    minor_ver = Column(BigInteger, index=True)
    build_ver = Column(BigInteger, index=True)

    created_date = Column(DateTime, default=datetime.now, index=True)
    comment = Column(String)
    url = Column(String)
    size = Column(BigInteger)

    # Package relationship
    package_id = Column(String, ForeignKey('packages.id'))
    package = orm.relationship("Package", back_populates='releases')

    @property
    def vesion_text(self):
        return f'{self.major_ver}.{self.minor_ver}.{self.build_ver}'