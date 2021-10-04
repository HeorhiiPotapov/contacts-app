from django.db import models
from django.contrib.auth.models import AbstractUser


class EnhancedUserManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

    def all(self):
        qs = self.get_queryset()
        return qs


class EnhancedUser(AbstractUser):
    pass
