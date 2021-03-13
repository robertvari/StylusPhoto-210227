def image_generator(photo_number, resolution=(800, 600)):
    photo_links = []

    for i in range(photo_number):
        photo_links.append(f"https://source.unsplash.com/{resolution[0]}x{resolution[1]}/?nature{i},water{i}")

    return photo_links