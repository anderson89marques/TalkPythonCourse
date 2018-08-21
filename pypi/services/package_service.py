from sqlalchemy.orm import joinedload

from pypi.models import Package, Release
from typing import List

def package_count(dbsession) -> int:
    return dbsession.query(Package).count()

def release_count(dbsession) -> int:
    return dbsession.query(Release).count()

def lastest_releases(dbsession, limit=10) -> List[Package]:

    releases = dbsession.query(Release)\
        .order_by(Release.created_date.desc())\
        .limit(limit*2)
    
    package_order_ids = [r.package_id for r in releases]
    package_ids = set(package_order_ids)

    packages = {p.id: p for p in dbsession.query(Package).filter(Package.id.in_(package_ids))}
    
    results = []
    for r in releases:
        if len(results) >= limit:
            break
        results.append(packages[r.package_id])

    return set(results)

def find_by_name(dbsession, package_name):
    #.options(joinedload(Package.releases))\
    package = dbsession.query(Package)\
        .filter(Package.id == package_name)\
        .first()
    return package