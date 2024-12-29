# middleware.py
from django.http import HttpResponseForbidden
from django.core.exceptions import PermissionDenied
from django.contrib.auth import get_user_model

User = get_user_model()

class BlockInvalidPasswordResetMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == '/password/reset/' and request.method == 'POST':
            email = request.POST.get('email')
            if email and not User.objects.filter(email=email).exists():
                raise PermissionDenied("Invalid password reset request")
        return self.get_response(request)
