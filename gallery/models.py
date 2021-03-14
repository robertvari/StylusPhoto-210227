from django.db import models


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
        pass

    def __str__(self):
        return self.title