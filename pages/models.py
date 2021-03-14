from django.db import models


class Contact(models.Model):
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200)
    facebook = models.URLField(max_length=200, blank=True)
    instagram = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.email


class HomePage(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    content = models.TextField(max_length=2000)

    def __str__(self):
        return self.title