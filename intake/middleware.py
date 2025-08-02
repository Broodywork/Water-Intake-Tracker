from django.shortcuts import redirect
from django.conf import settings

class LoginRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        protected_paths = ['/add', '/edit', '/delete', '/compare', '/list']

        if not request.user.is_authenticated:
            for path in protected_paths:
                if request.path.startswith(path):
                    return redirect(f'{settings.LOGIN_URL}?next={request.path}')
                    
        response = self.get_response(request)
        return response
