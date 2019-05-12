from engine.views import View
from engine.serializer import to_json


class Route(View):
    def data(self):
        user = self.user()
        room = user.room
        return to_json(room)
