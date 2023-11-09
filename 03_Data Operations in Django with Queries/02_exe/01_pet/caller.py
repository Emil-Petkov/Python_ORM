import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Pet


def create_pet(name, species):
    Pet.objects.create(
        name=name,
        species=species
    )

    return f"{name} is a very cute {species}!"


print(create_pet('Buddy', 'Dog'))
print(create_pet('Whiskers', 'Cat'))
print(create_pet('Rocky', 'Hamster'))
