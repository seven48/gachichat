""" Route for getting info about created user """

from engine.views import View


class Route(View):
    def data(self):
        user = self.user()
        return {
            'first_name': user.first_name,
            'last_name': user.last_name
        }
