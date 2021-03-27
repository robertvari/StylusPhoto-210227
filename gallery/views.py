from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Category, Photo


class GalleryView(TemplateView):
    template_name = "gallery.html"

    photos = Photo.objects.all()
    extra_context = {
        "categories": Category.objects.all(),
        "photos": photos
    }


def photo_details(request, slug):
    context = {
        "photo": f"https://source.unsplash.com/1600x900/?nature{slug},water{slug}",
        "title": "Ez itt a kép",
        "subtitle": "2020 aug. 1.",
        "content": "A kép leírása...",
    }

    return render(request, "photo_details.html", context)