from django.urls import path

from .views import HomeView, ContactView, AboutView, ContactSentView

urlpatterns = [
    path('', HomeView.as_view()),
    path('about/', AboutView.as_view()),
    path('contact/', ContactView.as_view()),
    path('contact/sent/', ContactSentView.as_view()),
]