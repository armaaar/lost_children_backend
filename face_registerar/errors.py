from helpers.error_response import error_response

APP_HANDLER = 'FR'

ERRORS: dict = {
    'no_face': 'No faces could be detected',
}

def err(err_name: str) -> str:
    """return json response for error"""
    return error_response(err_name, ERRORS, APP_HANDLER)
