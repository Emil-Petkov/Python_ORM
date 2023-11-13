import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import ArtworkGallery, Laptop
from django.db.models import Q, Case, When, Value, F


def show_highest_rated_art():
    best_artwork = ArtworkGallery.objects.order_by("-rating", "id").first()

    return f"{best_artwork.art_name} is the highest-rated art with a {best_artwork.rating} rating!"


def bulk_create_arts(first_art, second_art):
    ArtworkGallery.objects.bulk_create([
        first_art,
        second_art,
    ])


def delete_negative_rated_arts():
    ArtworkGallery.objects.filter(rating__lt=0).delete()


def show_the_most_expensive_laptop():
    best_laptop = Laptop.objects.order_by("-price", "id").first()

    return f"{best_laptop.brand} is the most expensive laptop available for {best_laptop.price}$!"


def bulk_create_laptops(*args):
    Laptop.objects.bulk_create(*args)


def update_to_512_GB_storage():
    # Laptop.objects.filter(
    #     brand__in=[
    #         "Asus",
    #         "Lenovo"
    #     ]
    # ).update(storage=512)

    Laptop.objects.filter(Q(brand="Asus") | Q(brand="Lenovo")).update(storage=512)


def update_to_16_GB_memory():
    # Laptop.objects.filter(
    #     brand__in=[
    #         "Apple",
    #         "Dell",
    #         "Acer"
    #     ]
    # ).update(storage=16)

    Laptop.objects.filter(Q(brand="Apple") | Q(brand="Dell") | Q(brand="Acer")).update(memory=16)


def update_operation_systems():
    Laptop.objects.update(
        operation_system=Case(
            When(brand="Asus", then=Value("Windows")),
            When(brand="Apple", then=Value("MacOS")),
            When(brand__in=["Acer", "Dell"], then=Value("Linux")),
            When(brand="Lenovo", then=Value("Chrome OS")),
            default=F("operation_system"),
        )
    )

    # Laptop.objects.filter(brand="Asus").update(operation_systems="Windows")
    # Laptop.objects.filter(brand="Apple").update(operation_systems="MacOS")
    # Laptop.objects.filter(brand__in=["Dell", "Acer"]).update(operation_systems="Linux")
    # Laptop.objects.filter(brand="Lenovo").update(operation_systems="Chrome OS")


def delete_inexpensive_laptops():
    Laptop.objects.filter(price__lt=1200).delete()
