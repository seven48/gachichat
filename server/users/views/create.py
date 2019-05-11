from engine.views import View
from rooms.models import Room
from users.models import UserProfile


class Route(View):
    def data(self):
        password = self.request.json.get('password')
        room_id = self.request.json.get('room_id')
        if room_id is None:
            raise Exception('Attribute "room_id" is not specified')
        room = Room.objects.filter(id=room_id).first()
        if not room:
            raise Exception('Room is not found')
        if room.password:
            if password:
                if not Room.objects.verify_pass(room.password, password):
                    raise Exception('Room password is incorrect')
            else:
                raise Exception('Room is under control. Enter password')
        return UserProfile.objects.new_user(
            room=room
        )
