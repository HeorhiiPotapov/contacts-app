from django.db import models


class Contact(models.Model):
    """to simple to write as mutch about it"""
    name = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=255, null=True)

    def __str__(self):
        return f"{self.name}{self.email}"

    def __unicode__(self):
        return
