""" Route for getting info about created user """

from users.models import UserProfile
from utils.views import View


class Route(View):
    def data(self):
        if not self.request.META.get('HTTP_AUTHORIZATION'):
            raise Exception('Authorization token is missing')
        user = UserProfile.objects.decode_token(
            self.request.META['HTTP_AUTHORIZATION']
        )
        return {
            'first_name': user.first_name,
            'last_name': user.last_name
        }
