from django.views.generic import TemplateView
from utilities.mock_data import image_generator
import random

from .models import HomePage, AboutPageModel
from gallery.models import Photo


class HomeView(TemplateView):
    template_name = "home.html"

    extra_context = {
        "photos": Photo.objects.filter(frontpage=True)
    }

    homepage_content = HomePage.objects.all()
    if homepage_content:
        extra_context["title"] = homepage_content[0].title
        extra_context["subtitle"] = homepage_content[0].subtitle
        extra_context["content"] = homepage_content[0].content


class AboutView(TemplateView):
    template_name = "about.html"

    photos = Photo.objects.all()

    extra_context = {
        "photo": random.choice(photos)
    }

    about_content = AboutPageModel.objects.all()
    if about_content:
        extra_context["title"] = about_content[0].title
        extra_context["subtitle"] = about_content[0].subtitle
        extra_context["content"] = about_content[0].content


class ContactView(TemplateView):
    template_name = "contact.html"
    extra_context = {
        "title": "Kérjen tőlünk ajánlatot",
        "photos": image_generator(1)
    }