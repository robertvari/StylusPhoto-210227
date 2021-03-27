from django.contrib import admin

from .models import Category, Photo

admin.site.register(Category)


class PhotoModelAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "frontpage"]
    list_filter = ["category"]
    list_editable = ["category", "frontpage"]

admin.site.register(Photo, PhotoModelAdmin)