from django.db import models
from django.contrib.auth.models import AbstractUser

# anonymous, verified, associated


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField('Email', unique=True)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
