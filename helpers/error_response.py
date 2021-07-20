import json
from django.http.response import HttpResponseBadRequest

def error_response(
    err_name: str = 'unknown',
    errors: dict = None,
    handler: str = 'GNR'
):
    """return json response for error"""
    return HttpResponseBadRequest(json.dumps({
        'code': 'ERR:{0}:{1}'.format(handler, err_name),
        'message': errors[err_name]
            if isinstance(errors, dict) and err_name in errors
            else 'Unknown error'
    }))
