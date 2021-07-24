import json
from django.http import HttpResponseBadRequest, JsonResponse

def unified_response(
    message_name: str = None,
    messages: dict = None,
    handler: str = 'GNR',
    is_error: bool = False,
    fields: dict = None
):
    """Generate json response"""
    default: dict = {
        'handler': 'ERR' if is_error else 'OK',
        'message': 'Unknown error' if is_error else 'Request was successful'
    }
    response_object: dict = {
        'code': '{0}:{1}:{2}'.format(default['handler'], handler, message_name),
        'message': messages[message_name]
            if isinstance(messages, dict) and message_name in messages
            else default['message']
    }
    if isinstance(fields, dict):
        response_object.update(fields)

    if is_error:
        return HttpResponseBadRequest(json.dumps(response_object))

    return JsonResponse(response_object)
