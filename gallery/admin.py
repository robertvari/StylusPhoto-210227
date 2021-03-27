from django.contrib import admin

from .models import Category, Photo

admin.site.register(Category)


class PhotoModelAdmin(admin.ModelAdmin):
    list_display = ["title", "category"]
    list_filter = ["category"]

admin.site.register(Photo, PhotoModelAdmin)