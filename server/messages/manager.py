from django.db import models


class MessageManager(models.Manager):
    def send(self, text, user):
        message = self.create(
            user=user,
            room=user.room,
            text=text
        )

        return {
            'id': message.id,
            'text': message.text,
            'created': int(message.datetime.timestamp()),
            'user': {
                'id': user.id
            },
            'room': {
                'id': user.room.id
            }
        }
