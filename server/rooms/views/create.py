from engine.views import View
from rooms.models import Room


class Route(View):
    def data(self):
        options = {}
        if self.request.json.get('password'):
            options['password'] = self.request.json.get('password'),
        if self.request.json.get('name'):
            options['name'] = self.request.json.get('name'),
        if self.request.json.get('description'):
            options['description'] = self.request.json.get('description'),

        return Room.objects.new_room(**options)
