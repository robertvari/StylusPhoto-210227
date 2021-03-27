from django.views.generic import TemplateView, FormView
import random

from .models import HomePage, AboutPageModel
from gallery.models import Photo
from .forms import ContactForm


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


class ContactView(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = "/contact/sent/"

    extra_context = {
        "title": "Kérjen tőlünk ajánlatot",
    }

    def form_valid(self, form):
        print(form.data["name"])
        print(form.data["email"])
        print(form.data["message"])

        # todo send email for me!
        # use SendGrid for sending out emails

        return super().form_valid(form)



class ContactSentView(TemplateView):
    template_name = "email_sent.html"
