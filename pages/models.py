from django.db import models


class Contact(models.Model):
    email = models.EmailField(max_length=200)
    phone = models.TextField(max_length=200)
    facebook = models.URLField(max_length=200, blank=True)
    instagram = models.URLField(max_length=200, blank=True)