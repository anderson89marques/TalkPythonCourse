from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError


def get_test_packages():
    return [
        {"name": 'requests', "version": '1.2.4'},
        {"name": 'sqlalchemy', "version": '2.0.0'},
        {"name": 'pyramid', "version": '1.9.2'}
    ]


@view_config(route_name='home', renderer='pypi:templates/home/home_index.jinja2')
def home_index(request):
    return {
        'packages': get_test_packages()
    }