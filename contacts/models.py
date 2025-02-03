from django.db import models

# Create your models here.


class Contact(models.Model):
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=100)
    sender = models.EmailField()
    cc_myself = models.BooleanField(null=True, blank=True)
