from django.db import models
from django.contrib.auth.models import AbstractUser


class EnhancedUserManager(models.Manager):
    def all(self):
        qs = super(EnhancedUser, self).filter(user_activation=True)
        return qs


class EnhancedUser(AbstractUser):
    name = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=255, null=True)

    objects = EnhancedUserManager()

    def __str__(self):
        return

    def __unicode__(self):
        return
