import hashlib
import binascii
import os

import requests
from django.db import models

from users.models import UserProfile


class RoomManager(models.Manager):
    @staticmethod
    def hash_pass(password):
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        pwdhash = hashlib.pbkdf2_hmac(
            'sha512',
            password.encode('utf-8'),
            salt,
            100000
        )
        pwdhash = binascii.hexlify(pwdhash)
        return (salt + pwdhash).decode('ascii')

    @staticmethod
    def verify_pass(hashed, password):
        salt = hashed[:64]
        stored_password = hashed[64:]
        pwdhash = hashlib.pbkdf2_hmac(
            'sha512',
            password.encode('utf-8'),
            salt.encode('ascii'),
            100000
        )
        pwdhash = binascii.hexlify(pwdhash).decode('ascii')
        return pwdhash == stored_password

    def new_room(self, **kwargs):
        room_creating_data = {}
        if kwargs.get('password'):
            room_creating_data['password'] = self.hash_pass(kwargs['password'])
        if kwargs.get('name'):
            room_creating_data['name'] = kwargs['name']
        if kwargs.get('description'):
            room_creating_data['description'] = kwargs['description']
        room = self.create(**room_creating_data)
        user = UserProfile.objects.new_user(
            room=room
        )
        room_info = {}
        room_info['id'] = room.id
        room_info['name'] = room.name
        room_info['description'] = room.description
        room_info['created'] = int(room.created.timestamp())
        if kwargs.get('password'):
            room_info['password'] = kwargs['password']

        return {
            'user': user,
            'room': room_info
        }

    @staticmethod
    def get_room_name():
        data = requests.get('http://names.drycodes.com/1')
        name = data.json()[0]
        return name
