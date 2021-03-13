from django.shortcuts import render
from utilities.mock_data import image_generator


def gallery_view(request):
    context = {
        "categories": ["Wedding", "Nature", "Sport"],
        "photos": image_generator(50)
    }

    return render(request, "gallery.html", context)


def photo_details(request, slug):
    context = {
        "photo": f"https://source.unsplash.com/1600x900/?nature{slug},water{slug}",
        "title": "Ez itt a kép",
        "subtitle": "2020 aug. 1.",
        "content": "A kép leírása...",
    }

    return render(request, "photo_details.html", context)