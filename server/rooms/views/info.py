from engine.views import View


class Route(View):
    def data(self):
        user = self.user()
        room = user.room
        return {
            'name': room.name,
            'description': room.description,
            'link': room.link,
            'created': int(room.created.timestamp())
        }
