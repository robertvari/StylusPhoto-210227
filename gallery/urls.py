from django.urls import path

from .views import GalleryView, photo_details

urlpatterns = [
    path('', GalleryView.as_view()),
    path('<str:slug>/', photo_details)
]