from django.urls import path


class Router(list):
    def get(self, url, func):
        self.append(path(url, func.methods(['GET'])))

    def post(self, url, func):
        self.append(path(url, func.methods(['POST'])))

    def register(self, url, func, methods=[]):
        self.append(
            path(url, func.methods(methods))
        )
