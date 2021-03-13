from django.shortcuts import render
from utilities.mock_data import image_generator


def home_view(request):
    # todo create a model for this
    context = {
        "title": "photographica",
        "subtitle": "Ahol a fotó és a grafika találkozik",
        "content": "Grafikus vagyok, és fotós. Kreatív képeimmel szeretném azt megmutatni, ami nem létezik (vagy mégis?) Célom, hogy az emberek megálljanak képeim előtt és elgondolkozzanak. Érezzenek valamit, csodálkozzanak, szeressék, gyűlöljék, de mindenképp érzéseket váltson ki. Ne egyszerűen csak elmenjenek előtte, továbblépjenek. És ha valaki visszatér, hogy újra megnézze, akkor már boldog vagyok.",
        "photos": image_generator(5)
    }

    return render(request, "home.html", context)


def about_view(request):
    # todo create a model for this
    context = {
        "title": "Hogyan is készülnek a képeim?",
        "subtitle": "",
        "content": "Előszőr is tervezéssel! Sokat rajzolok, vázlatokat készítek a fotózások előtt. Egyrészt, szeretek koncepcióval készülni, és szeretnék az ügyfélhez, modellhez legjobban illő ötletekkel előállni. A fotózásra emiatt felkészülten érkezek, és lehet is a koncepció kivitelezésével foglalkozni.",
        "photos": image_generator(1)
    }

    return render(request, "about.html", context)


def contact_view(request):
    # todo create a model for this
    context = {
        "title": "Kérjen tőlünk ajánlatot",
        "subtitle": "",
        "content": "",
        "photos": image_generator(1)
    }

    return render(request, "contact.html", context)
