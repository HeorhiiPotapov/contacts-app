from django.db import models


class ContactModelManager(models.Model):
    def all(self):
        qs = super(ContactModelManager, self).get_queryset()

    def verified(self):
        qs = self.all().filter(
            id__in=[i for i in range(1, 10000)], verified=True)
        return qs

    def inactive(self):
        qs = self.all().filter(inactive=True)
        return qs

    def read_only(self) ->


class Contact(models.Model):
    id = models.BigIntegerField(primary_key=True,
                                blank=True,
                                unique=True,
                                default=0)
    name = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=255, null=True)

    objects = ContactModelManager()

    def __str__(self):
        return self.name
