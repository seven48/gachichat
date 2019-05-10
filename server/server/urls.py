""" Main url configuration """


from django.urls import path, include

from users.urls import router as users_router
from rooms.urls import router as rooms_router


urlpatterns = [
    path(r'users/', include(users_router)),
    path(r'rooms/', include(rooms_router))
]
