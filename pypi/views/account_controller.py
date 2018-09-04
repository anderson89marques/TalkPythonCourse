from pyramid.view import view_config
from pyramid.request import Request
from pyramid.httpexceptions import HTTPFound
from pyramid.security import forget, remember

import pypi.services.user_service as user_service


#### INDEX ####
@view_config(route_name='account_home',
             renderer='pypi:templates/account/index.jinja2',
             request_method="GET")
def index(request):
    return {}


#### LOGIN ####
@view_config(route_name='login', 
             renderer='pypi:templates/account/login.jinja2',
             request_method="GET")
def login_get(request):
    return {}

@view_config(route_name='login', 
             renderer='pypi:templates/account/login.jinja2',
             request_method="POST")
def login_post(request: Request):
    print(f'POST: {request.POST}')
    email = request.POST.get('email')
    password = request.POST.get('password')
    
    user = user_service.login_user(request.dbsession, email, password)
    print(user)
    if not user:
        error = "The user could not be found or the password is incorrect"
        return {
            'email': email,
            'password': password,
            'error': error
        }
    
    # TODO: login user (session)
    headers = remember(request, user.id)
    return HTTPFound(location='/account', headers=headers)

#### REGISTER ####

@view_config(route_name='register', 
             renderer='pypi:templates/account/register.jinja2',
             request_method="GET")
def register_get(_):
    return {
            'name': '',
            'email': '',
            'password': '',
            'error': None
        }

@view_config(route_name='register', 
             renderer='pypi:templates/account/register.jinja2',
             request_method="POST")
def register_post(request: Request):
    print(f'POST: {request.POST}')
    email = request.POST.get('email')
    name = request.POST.get('name')
    password = request.POST.get('password')
    
    if not email or not name or not password:
        error = "Some required field are missing"
        return {
            'name': name,
            'email': email,
            'password': password,
            'error': error
        }
    
    # create user
    user_service.create_user(request.dbsession, name, email, password)
    return HTTPFound(location='/account')

#### LOGOUT ####

@view_config(route_name="logout")
def logout(request):
    headers = forget(request)
    return HTTPFound(location='/', headers=headers)