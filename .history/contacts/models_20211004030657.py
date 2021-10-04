from django.db import models


class ContactModelManager(models.Model):
    def all(self):
        qs = super(ContactModelManager, self).get_queryset()


class Contact(models.Model):
    id = models.BigIntegerField(primary_key=True,
                                blank=True,
                                max_length=20,
                                default=0)
    name = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=255, null=True)

    objects = ContactModelManager()

    def __str__(self):
        return self.name
