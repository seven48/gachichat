from engine.views import View
from rooms.models import Room


class Route(View):
    def data(self):
        return Room.objects.new_room(**self.request.json.dict)
