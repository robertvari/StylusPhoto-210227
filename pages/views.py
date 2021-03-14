from django.shortcuts import render
from utilities.mock_data import image_generator

from .models import HomePage


def home_view(request):
    homepage_content = HomePage.objects.all()
    context = {
        "title": "",
        "subtitle": "",
        "content": "",
        "photos": image_generator(5)
    }

    if homepage_content:
        context["title"] = homepage_content[0].title
        context["subtitle"] = homepage_content[0].subtitle
        context["content"] = homepage_content[0].content

    return render(request, "home.html", context)


def about_view(request):
    # todo create a model for this
    context = {
        "title": "Hogyan is készülnek a képeim?",
        "subtitle": "",
        "content": "Előszőr is tervezéssel! Sokat rajzolok, vázlatokat készítek a fotózások előtt. Egyrészt, szeretek koncepcióval készülni, és szeretnék az ügyfélhez, modellhez legjobban illő ötletekkel előállni. A fotózásra emiatt felkészülten érkezek, és lehet is a koncepció kivitelezésével foglalkozni.",
        "photos": image_generator(1)
    }

    return render(request, "about.html", context)


def contact_view(request):
    # todo create a model for this
    context = {
        "title": "Kérjen tőlünk ajánlatot",
        "subtitle": "",
        "content": "",
        "photos": image_generator(1)
    }

    return render(request, "contact.html", context)
