from users.models import UserProfile
from utils.views import View


class View(View):
    @staticmethod
    def data():
        return UserProfile.objects.new_user()
