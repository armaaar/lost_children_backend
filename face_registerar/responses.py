from helpers.unified_response import unified_response

_APP_HANDLER = 'FR'

_ERRORS: dict = {
    'no_face': 'No faces could be detected',
    'no_image_by_id': 'Requested image can\'t be found'
}

_MESSAGES: dict = {
    'image_uploaded': 'Image uploaded successfully',
    'faces_confirmed': 'Faces confirmed successfully',
    'image_deleted': 'Image deleted successfully'
}

def error(err_name: str = None, fields: dict = None) -> str:
    """return json response for error"""
    return unified_response(
        message_name = err_name,
        messages = _ERRORS,
        handler = _APP_HANDLER,
        is_error = True,
        fields = fields,
    )

def success(message_name: str = None, fields: dict = None) -> str:
    """return json response for successful requests"""
    return unified_response(
        message_name = message_name,
        messages = _MESSAGES,
        handler = _APP_HANDLER,
        is_error = False,
        fields = fields,
    )
