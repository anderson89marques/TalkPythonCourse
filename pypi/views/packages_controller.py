from pyramid.view import view_config
from pyramid.request import Request
import pyramid.httpexceptions as exc

from pypi.services import package_service


# /project/{project_name}
@view_config(route_name='package_details', renderer='pypi:templates/packages/details.jinja2')
def details(request: Request):
    package_name = request.matchdict.get('package_name')
    package = package_service.find_by_name(request.dbsession, package_name)

    if not package:
        raise exc.HTTPNotFound()

    latest_version = '0.0.0'
    latest_release = None

    if package.releases:
        latest_release = package.releases[0]
        latest_version = f'{latest_release.major_ver}{latest_release.minor_ver}{latest_release.build_ver}'

    return {
        'package': package,
        'latest_version': latest_version,
        'latest_release': latest_release,
        'release_version': latest_version,
        'maintainers': [],
        'is_latest': True
    }


# /project/{project_name}/releases
@view_config(route_name='releases', renderer='pypi:templates/packages/releases.jinja2')
def releases(request: Request):
    package_name = request.matchdict.get('package_name')
    if not package_name:
        raise exc.HTTPNotFound()

    return {
        'package_name': package_name,
        'releases': []
    }


# /project/{project_name}/releases/{release_version}
@view_config(route_name='release_version', renderer='pypi:templates/packages/details.jinja2')
def release_version(request: Request):
    package_name = request.matchdict.get('package_name')
    release_version = request.matchdict.get('release_version')
    if not package_name:
        raise exc.HTTPNotFound()

    return {
        'package_name': package_name,
        'release_version': release_version,
        'releases': []
    }

# /{num}
@view_config(route_name='popular', renderer='pypi:templates/packages/details.jinja2')
def popular(request: Request):
    num = int(request.matchdict.get('num'))
    if not (1 <= num or num <= 10):
        raise exc.HTTPNotFound()

    return {
        'package_name': f"The {num}th popular package."
    }