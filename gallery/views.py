from django.shortcuts import render
from utilities.mock_data import image_generator


def gallery_view(request):
    context = {
        "categories": ["Wedding", "Nature", "Sport"],
        "photos": image_generator(50)
    }

    return render(request, "gallery.html", context)