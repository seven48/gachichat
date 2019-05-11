from engine.views import View
from users.models import UserProfile
from messages.models import Messages


class Route(View):
    def data(self):
        if not self.request.META.get('HTTP_AUTHORIZATION'):
            raise Exception('Authorization token is missing')
        user = UserProfile.objects.decode_token(
            self.request.META['HTTP_AUTHORIZATION']
        )
        text = self.request.json.get('text')
        if not text:
            raise Exception('Attribute "text" is not specified')
        return Messages.objects.send(
            text=text,
            user=user
        )
