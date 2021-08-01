import json
from django.core import serializers
from django.db.models.base import Model

def _model_to_value(model: dict):
    value: dict = {'id': model['pk']}
    value.update(model['fields'])
    return value


def models_to_serializable(models: list[Model]) -> list:
    """Convert django model object to something that can be json serialized"""
    tmp_json = serializers.serialize("json", models)
    return list(map(_model_to_value, json.loads(tmp_json)))
