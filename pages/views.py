from django.shortcuts import render
from django.views.generic import TemplateView
from utilities.mock_data import image_generator

from .models import HomePage


class HomeView(TemplateView):
    template_name = "home.html"

    extra_context = {
        "photos": image_generator(5)
    }

    homepage_content = HomePage.objects.all()
    if homepage_content:
        extra_context["title"] = homepage_content[0].title
        extra_context["subtitle"] = homepage_content[0].subtitle
        extra_context["content"] = homepage_content[0].content


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
