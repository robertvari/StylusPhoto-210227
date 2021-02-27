from django.shortcuts import render, HttpResponse


def home_view(request):
    return HttpResponse("Hello World")


def contact_view(request):
    return HttpResponse("Contact page")


def about_view(request):
    return HttpResponse("About page")