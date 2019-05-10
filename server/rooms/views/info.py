from engine.views import View
from users.models import UserProfile


class Route(View):
    def data(self):
        if not self.request.META.get('HTTP_AUTHORIZATION'):
            raise Exception('Authorization token is missing')
        user = UserProfile.objects.decode_token(
            self.request.META['HTTP_AUTHORIZATION']
        )
        room = user.room
        return {
            'name': room.name,
            'description': room.description,
            'link': room.link,
            'created': int(room.created.timestamp())
        }
