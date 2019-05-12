from engine.views import View
from rooms.models import Room
from users.models import UserProfile
from engine.exceptions import APIException


class Route(View):
    def data(self):
        password = self.request.json.get('password', required=False)
        room_id = self.request.json.get('room_id', required=True)
        room = Room.objects.filter(id=room_id).first()
        if not room:
            raise APIException('Room is not found')
        if room.password:
            if password:
                if not Room.objects.verify_pass(room.password, password):
                    raise APIException('Room password is incorrect')
            else:
                raise APIException('Room is under control. Enter password')
        return UserProfile.objects.new_user(
            room=room
        )
