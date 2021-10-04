from django.db import models
from django.contrib.auth.models import AbstractUser


class EnhancedUserManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

    def all(self):
        super(EnhancedUser, self).filter(uwerActivation=True)
        return


class EnhancedUser(AbstractUser):
    pass
