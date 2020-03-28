from django.conf import settings
from django.db import models


class Contact(models.Model):
    "Generated Model"
    contact_id = models.BigIntegerField()
    firstname = models.TextField()
    lastname = models.TextField()
    jobtitle = models.TextField()
    email = models.EmailField(max_length=254,)


# Create your models here.
