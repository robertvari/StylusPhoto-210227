from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Category, Photo


class GalleryView(ListView):
    template_name = "gallery.html"
    model = Photo
    context_object_name = "photos"

    extra_context = {
        "categories": Category.objects.all(),
    }

    def get_queryset(self):
        category_name = self.request.GET.get("category")
        if category_name:
            photos = Photo.objects.filter(category__title=category_name)
        else:
            photos = Photo.objects.all()

        return photos


def photo_details(request, slug):
    context = {
        "photo": f"https://source.unsplash.com/1600x900/?nature{slug},water{slug}",
        "title": "Ez itt a kép",
        "subtitle": "2020 aug. 1.",
        "content": "A kép leírása...",
    }

    return render(request, "photo_details.html", context)


class PhotoDetailView(DetailView):
    model = Photo
    template_name = "photo_details.html"
    context_object_name = "photo"