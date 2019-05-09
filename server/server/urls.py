""" Main url configuration """


from django.urls import path, include

from users.urls import URLS as users_router


urlpatterns = [
    path(r'users/', include(users_router))
]
