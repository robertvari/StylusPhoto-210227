from django.shortcuts import render


def image_generator(photo_number, resolution=(800, 600)):
    photo_links = []

    for i in range(photo_number):
        photo_links.append(f"https://source.unsplash.com/{resolution[0]}x{resolution[1]}/?nature{i},water{i}")

    return photo_links


def home_view(request):
    context = {
        "title": "photographica",
        "subtitle": "Ahol a fotó és a grafika találkozik",
        "content": "Grafikus vagyok, és fotós. Kreatív képeimmel szeretném azt megmutatni, ami nem létezik (vagy mégis?) Célom, hogy az emberek megálljanak képeim előtt és elgondolkozzanak. Érezzenek valamit, csodálkozzanak, szeressék, gyűlöljék, de mindenképp érzéseket váltson ki. Ne egyszerűen csak elmenjenek előtte, továbblépjenek. És ha valaki visszatér, hogy újra megnézze, akkor már boldog vagyok.",
        "photos": image_generator(5)
    }

    return render(request, "home.html", context)


def contact_view(request):
    return render(request, "contact.html")


def about_view(request):
    return render(request, "about.html")


def gallery_view(request):
    context = {
        "photos": image_generator(50)
    }

    return render(request, "gallery.html", context)