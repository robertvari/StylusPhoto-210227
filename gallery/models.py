from django.db import models
from django.db.models.signals import post_delete, pre_save
from PIL import Image
import os


class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Photo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="photos")
    description = models.TextField(max_length=1000)

    uploaded = models.DateTimeField(auto_now_add=True)

    slug = models.SlugField(max_length=200, blank=True)

    def save(self, *args, **kwargs):
        # before save if image replaced?
        self.replace_image()

        super(Photo, self).save(*args, **kwargs)

        # after save resize image
        self.resize_image()

    def replace_image(self):
        try:
            photo = Photo.objects.get(id=self.id)
            if photo.image.name != self.image.name:
                photo.image.delete(save=False)
        except:
            pass

    def resize_image(self):
        image_path = self.image.path
        img = Image.open(image_path)

        max_size = 1500
        if img.size[0] > max_size or img.size[1] > max_size:
            img.thumbnail((max_size, max_size))
            img.save(image_path)

    def __str__(self):
        return self.title


def image_cleanup(sender, instance, **kwargs):
    if os.path.exists(instance.image.path):
        os.remove(instance.image.path)


post_delete.connect(image_cleanup, sender=Photo)
