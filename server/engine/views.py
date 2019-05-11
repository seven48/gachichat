""" Abstract views with error handlers etc """


import json

from datetime import datetime

from django.http import JsonResponse

from server.settings import DEBUG


class ABSView:
    """" Abstract view class """

    def __new__(cls, request, methods=None):
        """ Overriding class creating """
        inst = super(ABSView, cls).__new__(cls)
        inst.request = request
        inst.methods = methods

        if methods:
            if request.method not in methods:
                err = Exception(
                    'Method {} is not allowed'.format(
                        request.method
                    )
                )
                return inst._error(err)

        return inst._handler()

    def _handler(self):
        """ Error catcher """
        try:
            return self.response()
        except Exception as err:
            return self._error(err)

    def response(self):
        """ Build response data """
        return JsonResponse({
            'status': 'ok',
            'data': self.data()
        })

    @staticmethod
    def data():
        """ Getting data for response """
        return []

    @staticmethod
    def error(error):
        """ Method that is being called on error in "data" method """
        pass

    @staticmethod
    def error_message(error):
        """ Getting error message """
        return str(error)

    @staticmethod
    def error_status(error):
        """ Getting error status """
        return 500

    def _error(self, error):
        """ Private error handling """
        self.error(error)
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
    def get_JSON_body(self):
        if self.request.content_type == 'application/json':
            if self.request.body:
                return json.loads(self.request.body)
        return {}

    def _handler(self):
        try:
            self.request.json = self.get_JSON_body()
            return self.response()
        except json.JSONDecodeError:
            return self._error(Exception('JSON data is not valid'))
        except Exception as err:
            return self._error(err)


class LongPollingView(ABSView):
    def response(self):
        start = int(datetime.now().timestamp())

        while True:
            now = int(datetime.now().timestamp())

            data = self.data()
            if data:
                return JsonResponse(data)

            if now > start + 25:
                return JsonResponse([])
