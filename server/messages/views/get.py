from engine.views import View
from engine.serializer import to_json
from messages.models import Messages


class Route(View):
    def data(self):
        count = int(self.request.GET.get('count') or '50')
        offset = int(self.request.GET.get('offset') or '0')
        user = self.user()
        room = user.room
        queryset = Messages.objects.filter(room=room).order_by('-id')
        return [to_json(item) for item in queryset[offset:offset+count]]
