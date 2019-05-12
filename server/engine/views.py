from django.http import JsonResponse

from engine.exceptions import APIWrongMethod, APITokenError
from engine.body import JSONBody
from users.models import UserProfile


class ABSViewSet:
    def __new__(cls, request):
        inst = super(ABSViewSet, cls).__new__(cls)
        inst.request = request

        try:
            inst.request.json = JSONBody(
                inst.request.body,
                inst.request.content_type
            )

            response = {}
            response['status'] = 'success'
            response['data'] = inst.data()

            return JsonResponse(response)
        except Exception as err:
            inst.error()
            return inst._get_error(err)

    @staticmethod
    def _get_error(err):
        response = {}
        response['status'] = 'error'
        response['error'] = {}
        if hasattr(err, 'code'):
            response['error']['code'] = err.code
            response['error']['message'] = str(err)
        else:
            response['error']['code'] = 0
            response['error']['message'] = 'Unknown error'

        return JsonResponse(response, status=500)

    @classmethod
    def methods(cls, methods=[]):
        """ Setting allowed methods """
        def wrapper(request):
            if request.method not in methods:
                err = APIWrongMethod(request.method)
                return cls._get_error(err)
            return cls(request)
        return wrapper

    # USER METHODS
    @staticmethod
    def data():
        """ Getting data for response """
        return None

    @staticmethod
    def error():
        """ Method that is being called on error in "data" method """
        return None


class View(ABSViewSet):
    def user(self):
        if not self.request.META.get('HTTP_AUTHORIZATION'):
            raise APITokenError('Header "Authorization" is empty')
        return UserProfile.objects.decode_token(
            self.request.META['HTTP_AUTHORIZATION']
        )
