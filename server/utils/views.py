""" Abstract views with error handlers etc """


from django.http import JsonResponse

from server.settings import DEBUG


class WrongMethod(Exception):
    """ Request method is not allowed """
    pass  # pylint: disable=W0107


class ABSView:
    """" Abstract view class """

    @staticmethod
    def data():
        """ Getting data for response """
        return []

    @staticmethod
    def error(error):
        """ Method that is being called on error in "data" method """
        pass  # pylint: disable=W0107

    @staticmethod
    def error_message(error):
        """ Getting error message """
        return str(error)

    @staticmethod
    def error_status(error):  # pylint: disable=W0613
        """ Getting error status """
        return 500

    def _error(self, error):
        """ Private method with error handling """
        response = {}
        response['status'] = 'error'
        response['error'] = {}
        response['error']['message'] = self.error_message(error)
        if DEBUG:
            response['error']['name'] = error.__class__.__name__
        return JsonResponse(response, status=self.error_status(error))

    @classmethod
    def methods(cls, methods):
        """ Setting allowed methods """
        def wrapper(request):
            return cls(request, methods=methods)
        return wrapper


class View(ABSView):
    """ Higher level abstract view class """
    def __new__(cls, request, methods=None):
        """ Overriding class creating """
        inst = super(View, cls).__new__(cls)
        inst.request = request
        inst.methods = methods

        if methods:
            if request.method not in methods:
                err = WrongMethod(
                    'Method {} is not allowed'.format(
                        request.method
                    )
                )
                return inst._error(err)  # pylint: disable=W0212

        try:
            return JsonResponse({
                'status': 'success',
                'data': inst.data()
            })
        except Exception as err:  # pylint: disable=W0703
            inst.error(err)
            return inst._error(err)  # pylint: disable=W0212
