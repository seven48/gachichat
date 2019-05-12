from django.db import models


class MessageManager(models.Manager):
    def send(self, text, user):
        message = self.create(
            user=user,
            room=user.room,
            text=text
        )

        return message
