from users.models import UserProfile
from engine.views import View


class Route(View):
    @staticmethod
    def data():
        return UserProfile.objects.new_user()
