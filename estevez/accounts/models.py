from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class RegistroManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El correo electrónico es obligatorio')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class Registro(AbstractBaseUser):
    username = None
    email = models.EmailField(unique=True)
    nombre_completo = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField()
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre_completo', 'fecha_nacimiento']

    objects = RegistroManager()

    def __str__(self):
        return self.email
