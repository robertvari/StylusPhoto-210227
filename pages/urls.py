from django.urls import path

from .views import home_view, contact_view, about_view, gallery_view

urlpatterns = [
    path('', home_view),
    path('about/', about_view),
    path('contact/', contact_view),
    path('gallery/', gallery_view),
]