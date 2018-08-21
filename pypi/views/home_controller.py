from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from pypi.services import package_service, user_service


def get_test_packages():
    return [
        {"name": 'requests', "version": '1.2.4'},
        {"name": 'sqlalchemy', "version": '2.0.0'},
        {"name": 'pyramid', "version": '1.9.2'}
    ]


@view_config(route_name='home', renderer='pypi:templates/home/index.jinja2')
def index(request):
    return {
        'packages': package_service.lastest_releases(request.dbsession),
        'package_count': package_service.package_count(request.dbsession),
        'release_count': package_service.release_count(request.dbsession),
        'user_count': user_service.user_count(request.dbsession)
    }

@view_config(route_name='about', renderer='pypi:templates/home/about.jinja2')
def about(request):
    return {}