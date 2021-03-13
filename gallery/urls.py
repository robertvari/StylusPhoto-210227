from django.urls import path

from .views import gallery_view, photo_details

urlpatterns = [
    path('', gallery_view),
    path('<str:slug>/', photo_details)
]