from engine.views import View
from messages.models import Messages


def serializer(queryset, count, offset):
    def mapping(item):
        return {
            'id': item.id,
            'text': item.text,
            'created': int(item.datetime.timestamp()),
            'room': {
                'id': item.room.id
            },
            'user': {
                'id': item.user.id
            }
        }

    items = map(mapping, queryset[offset:offset+count])
    return list(items)


class Route(View):
    def data(self):
        count = int(self.request.GET.get('count') or '50')
        offset = int(self.request.GET.get('offset') or '0')
        user = self.user()
        room = user.room
        return serializer(
            Messages.objects.filter(room=room).order_by('-id'),
            count,
            offset
        )
