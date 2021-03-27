from django.urls import path

from .views import GalleryView, PhotoDetailView

urlpatterns = [
    path('', GalleryView.as_view()),
    path('<str:slug>/', PhotoDetailView.as_view())
]