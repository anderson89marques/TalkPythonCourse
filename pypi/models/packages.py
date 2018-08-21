from datetime import datetime

from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    String,
    DateTime,
    orm
)

from .meta import Base

from pypi.models.releases import Release


class Package(Base):
    __tablename__ = 'packages'
    id = Column(String, primary_key=True)
    created_date = Column(DateTime, default=datetime.now)
    summary = Column(String, nullable=True)
    description = Column(String, nullable=True)

    home_page = Column(String, nullable=True)
    docs_url = Column(String, nullable=True)
    package_url = Column(String, nullable=True)

    author_name = Column(String, nullable=True)
    author_email = Column(String, nullable=True, index=True)

    license = Column(String, index=True)

    releases = orm.relationship("Release", order_by=[
        Release.major_ver.desc(),
        Release.minor_ver.desc(),
        Release.build_ver.desc()
    ], back_populates='package')
    # mantainers

    def __repr__(self):
        return f'<Package {self.id}>'

# Index('my_index', Package.license, unique=True, mysql_length=255)
