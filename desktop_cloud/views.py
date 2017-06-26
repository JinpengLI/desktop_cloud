# -*- coding: utf-8 -*-

from pyramid.view import view_config
from pyramid.security import remember


@view_config(route_name='home', renderer='templates/index.jinja2')
def view_home(request):
    return {'title': 'Desktop Cloud'}

@view_config(route_name='signin', renderer='templates/signin.jinja2')
def view_signin(request):
    login = request.POST["login"]
    password = request.POST["password"]
    headers = remember(request,
        login, password=password, max_age='86400')
    response = request.response
    response.headerlist.extend(headers)
    return reponse

