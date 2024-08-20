import jwt
from config.JWT_SETTINGS import JWT_SETTINGS

from rest_framework.authentication import get_authorization_header


def tokenValidation(request):
    """
    It takes the token from the request header, decodes it, and returns the payload
    :param request: The request object that was sent to the view
    :return: The payload of the token.
    """
    token_header = get_authorization_header(request).decode("utf-8")
    token_header_split = token_header.split(" ")
    if token_header_split[0] == "Bearer":
        token = token_header_split[1]
        payload = jwt.decode(
            jwt=token, key=JWT_SETTINGS["SIGNING_KEY"], algorithms=["HS256"]
        )
        return payload
    else:
        return None
