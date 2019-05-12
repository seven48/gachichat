from engine.views import View
from engine.serializer import to_json
from messages.models import Messages


class Route(View):
    def data(self):
        user = self.user()
        text = self.request.json.get('text', required=True)
        message = Messages.objects.send(
            text=text,
            user=user
        )
        return to_json(message)
