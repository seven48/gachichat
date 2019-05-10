import json

from engine.views import View
from rooms.models import Room


class Route(View):
    def data(self):
        try:
            body = json.loads(self.request.body)
        except json.JSONDecodeError:
            return Room.objects.new_room()
        else:
            return Room.objects.new_room(**body)
