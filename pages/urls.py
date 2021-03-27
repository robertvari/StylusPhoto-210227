from django.urls import path

from .views import HomeView, contact_view, about_view

urlpatterns = [
    path('', HomeView.as_view()),
    path('about/', about_view),
    path('contact/', contact_view),
]