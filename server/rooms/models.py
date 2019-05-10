from django.db import models

from rooms.manager import RoomManager


class Room(models.Model):
    name = models.CharField(
        max_length=128,
        default=RoomManager.get_room_name,
        verbose_name='Room name'
    )
    description = models.TextField(
        verbose_name='Room description'
    )
    password = models.CharField(
        max_length=512,
        verbose_name='Room password hash'
    )
    link = models.CharField(
        max_length=128,
        verbose_name='Custom room link'
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Date of room creating'
    )

    objects = RoomManager()
