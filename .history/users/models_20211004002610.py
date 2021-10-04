from django.db import models
from django.contrib.auth.models import AbstractUser


class EnhancedUserManager(models.Manager):
    def all(self):
        qs = super(EnhancedUser, self).filter(user_activation=True)
        return qs


class EnhancedUser(AbstractUser):
    pass
