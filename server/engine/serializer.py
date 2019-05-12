from datetime import datetime

from django.db.models import Model


def to_json(model):
    response = {}

    for field in model.Serializer.fields:
        attr = getattr(model, field)
        if isinstance(attr, Model):
            response[field] = to_json(attr)
        elif isinstance(attr, datetime):
            response[field] = int(attr.timestamp())
        else:
            response[field] = attr

    return response
