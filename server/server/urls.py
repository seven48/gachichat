""" Main url configuration """


from django.urls import path, include

from users.urls import router as users_router
from rooms.urls import router as rooms_router
from messages.urls import router as messages_router


urlpatterns = [
    path('users/', include(users_router)),
    path('rooms/', include(rooms_router)),
    path('messages/', include(messages_router))
]
