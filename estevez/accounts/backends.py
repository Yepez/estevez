from django.contrib.auth.backends import BaseBackend
from .models import Registro

class RegistroBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None):
        try:
            registro = Registro.objects.get(email=email)
            if registro.check_password(password):
                return registro
        except Registro.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Registro.objects.get(pk=user_id)
        except Registro.DoesNotExist:
            return None