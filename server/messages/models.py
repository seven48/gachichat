from django.db import models

from messages.manager import MessageManager
from users.models import UserProfile
from rooms.models import Room


class Messages(models.Model):
    user = models.ForeignKey(
        UserProfile,
        models.CASCADE
    )
    room = models.ForeignKey(
        Room,
        models.CASCADE
    )
    text = models.TextField(
        null=False,
        blank=False
    )
    created = models.DateTimeField(
        auto_now_add=True
    )

    objects = MessageManager()

    class Serializer:
        fields = ('id', 'user', 'text', 'created')
