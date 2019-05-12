""" Route for getting info about created user """

from engine.views import View
from engine.serializer import to_json


class Route(View):
    def data(self):
        user = self.user()
        return to_json(user)
