from engine.views import View
from messages.models import Messages


class Route(View):
    def data(self):
        user = self.user()
        text = self.request.json.get('text', required=True)
        return Messages.objects.send(
            text=text,
            user=user
        )
