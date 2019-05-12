class APIException(Exception):
    """ Base exception for all API errors """

    code = 0
    message = 'API unknown error'

    def __init__(self, text=None):
        if text:
            Exception.__init__(self, text)
        else:
            Exception.__init__(self, self.message)


class APIWrongMethod(APIException):
    """ Wrong request method for API """

    code = 1
    message = 'Wrong method "{}" for method'

    def __init__(self, method):
        text = self.message.format(method)
        APIException.__init__(self, text)


class APITokenError(APIException):
    """ Access token invalid """

    code = 2
    message = 'Bad access token'


class APIMissingParameter(APIException):
    """ Required parameter is missing """

    code = 3
    message = 'Attribute "{}" is required'

    def __init__(self, param):
        text = self.message.format(param)
        APIException.__init__(self, text)
