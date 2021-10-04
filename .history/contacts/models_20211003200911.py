from django.db import models


class Contact(models.Model):
    id = models.BigIntegerField(primary_key=True, blank=True, defualt=)

    name = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=255, null=True)

    def __str__(self):
        return f"name: {self.name} Email: {self.email}"
