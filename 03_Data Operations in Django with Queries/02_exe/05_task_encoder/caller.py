import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Pet, Artifact, Location, Car, Task


def create_pet(name, species):
    Pet.objects.create(
        name=name,
        species=species
    )

    return f"{name} is a very cute {species}!"


def create_artifact(name, origin, age, description, is_magical):
    Artifact.objects.create(
        name=name,
        origin=origin,
        age=age,
        description=description,
        is_magical=is_magical,
    )


def delete_all_artifacts():
    Artifact.objects.all().delete()


def show_all_locations():
    locations = Location.objects.all().order_by('-id')

    return '\n'.join(str(l) for l in locations)


def new_capital():
    Location.objects.filter(pk=1).update(is_capital=True)

    # locations = Location.objects.first()
    # locations.is_capital = True
    # locations.save()


def get_capitals():
    return Location.objects.filter(is_capital=True).values("name")


def delete_first_location():
    Location.objects.first().delete()


def apply_discount():
    cars = Car.objects.all()

    for car in cars:
        percentage_off = sum(int(d) for d in str(car.year)) / 100
        discount = float(car.price) * percentage_off
        car.price_with_discount = float(car.price) - discount
        car.save()


def get_recent_cars():
    return Car.objects.filter(year__gte=2020).values("model", "price_with_discount")


def delete_last_car():
    Car.objects.last().delete()


def show_unfinished_tasks():
    unfinished_tasks = Task.objects.all().filter(is_finished=False)

    return '\n'.join(str(t) for t in unfinished_tasks)


def complete_odd_tasks():
    for task in Task.objects.all():
        if task.id % 2 != 0:
            task.is_finished = True
            task.save()


def encode_and_replace(text, task_title):
    decoding_text = ''.join(chr(ord(x) - 3) for x in text)
    Task.objects.filter(title=task_title).update(description=decoding_text)

    # task_matching = Task.objects.filter(title=task_title)
    # decoding_text = ''.join(chr(ord(x) - 3) for x in text)
    #
    # for task in task_matching:
    #     task.description = decoding_text
    #     task.save()


