from django.views.generic import TemplateView, FormView
from django.core.mail import send_mail
import random

from .models import HomePage, AboutPageModel
from gallery.models import Photo
from .forms import ContactForm


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context["photos"] = Photo.objects.filter(frontpage=True)

        homepage_content = HomePage.objects.all()
        if homepage_content:
            context["title"] = homepage_content[0].title
            context["subtitle"] = homepage_content[0].subtitle
            context["content"] = homepage_content[0].content

        return context


class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)

        photos = Photo.objects.all()

        if photos:
            context["photo"] = random.choice(photos)

        about_content = AboutPageModel.objects.all()
        if about_content:
            context["title"] = about_content[0].title
            context["subtitle"] = about_content[0].subtitle
            context["content"] = about_content[0].content

        return context


class ContactView(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = "/contact/sent/"

    extra_context = {
        "title": "Kérjen tőlünk ajánlatot",
    }

    def form_valid(self, form):
        # use SendGrid for sending out emails
        send_mail(
            "Contact",
            form.data["message"],
            form.data["email"],
            ['testaddress@gmail.com'],
            fail_silently=False
        )

        return super().form_valid(form)


class ContactSentView(TemplateView):
    template_name = "email_sent.html"
