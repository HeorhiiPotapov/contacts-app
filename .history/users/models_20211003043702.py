from django.db import models


class Contact(models.Model):

    """contact db model"""
    name = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=255, null=True)

    def __str__(self):
        return

    def __unicode__(self):
        return
