from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    wallet_address = models.CharField(max_length=256)
