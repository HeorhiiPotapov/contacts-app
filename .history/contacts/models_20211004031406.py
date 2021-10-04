from django.db import models


class ContactModelManager(models.Model):
    def all(self):
        qs = super(ContactModelManager, self).get_queryset()

    def verified(self):
        qs = self.all().filter(id__in=ids_list, verified=True)
        return qs

    def inactive(self) -> list():
        qs = self.all().filter(inactive=True)
        return qs\



class Contact(models.Model):
    id = models.BigIntegerField(primary_key=True,
                                blank=True,
                                max=20,
                                default=0)
    name = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=255, null=True)

    objects = ContactModelManager()

    def __str__(self):
        return self.name
