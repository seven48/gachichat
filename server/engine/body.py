import json

from engine.exceptions import APIException, APIMissingParameter


class JSONBody:
    def __init__(self, body, content_type=None):
        self.dict = self._parse_JSON_data(body, content_type)

    def get(self, key, required=False):
        value = self.dict.get(key)
        if value is None and required:
            raise APIMissingParameter(key)
        return value

    def _parse_JSON_data(self, body, content_type):
        if content_type == 'application/json':
            if body:
                try:
                    return json.loads(body)
                except json.JSONDecodeError:
                    raise APIException('Could not decode request body')
        return {}
