""" Users module urls """


from django.urls import path

from users.views import create, get_me


URLS = [
    path('create', create.Route.methods(['POST'])),
    path('getMe', get_me.Route.methods(['GET']))
]
