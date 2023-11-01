from django.db import models


# Create your models here.

class Shoe(models.Model):
    brand = models.CharField(
        max_length=25
    )
    size = models.PositiveIntegerField()


class UniqueBrands(models.Model):
    brand = models.CharField(
        max_length=25
    )


class EventRegistration(models.Model):
    event_name = models.CharField(
        max_length=60
    )
    participant_name = models.CharField(
        max_length=50
    )
    registration_date = models.DateField()

    def __str__(self):
        return f"{self.participant_name} - {self.event_name}"


class Movie(models.Model):
    title = models.CharField(
        max_length=100
    )

    director = models.CharField(
        max_length=100
    )

    release_year = models.PositiveIntegerField()

    genre = models.CharField(
        max_length=50
    )

    def __str__(self):
        return f'Movie "{self.title}" by {self.director}'