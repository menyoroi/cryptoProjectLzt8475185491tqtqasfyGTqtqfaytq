from django.http import HttpRequest
from django.core.cache import cache
import secrets


class SecurityPostRequestsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        if request.method == 'GET':
            new_key = secrets.token_hex(150)
            request.session['securityKey'] = new_key

        response = self.get_response(request)

        return response