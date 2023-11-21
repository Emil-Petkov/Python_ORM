








from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models

from main_app.validators import validate_name, validate_phone_number


class Customer(models.Model):
    name = models.CharField(
        max_length=100,
        validators=(
            validate_name,
        ),
    )

    age = models.PositiveIntegerField(
        validators=(
            MinValueValidator(18, message="Age must be greater than 18"),
        )
    )

    email = models.EmailField(
        error_messages={"invalid": "Enter a valid email address"}
    )

    phone_number = models.CharField(
        max_length=13,
        validators=(
            validate_phone_number,
        ),
    )

    website_url = models.URLField(
        error_messages={"invalid": "Enter a valid URL"},
    )


class BaseMedia(models.Model):
    class Meta:
        abstract = True
        ordering = ["-created_at", "title"]

    title = models.CharField(
        max_length=100,
    )

    description = models.TextField()

    genre = models.CharField(
        max_length=50,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )


class Book(BaseMedia):
    class Meta(BaseMedia.Meta):
        verbose_name = "Model Book"
        verbose_name_plural = "Models of type - Book"

    author = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(5, message="Author must be at least 5 characters long")
        ],
    )

    isbn = models.CharField(
        max_length=20,
        validators=[
            MinLengthValidator(6, message="ISBN must be at least 6 characters long")
        ],
    )


class Movie(BaseMedia):
    class Meta(BaseMedia.Meta):
        verbose_name = "Model Movie"
        verbose_name_plural = "Models of type - Movie"

    director = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(8, message="Director must be at least 8 characters long")
        ],
    )


class Music(BaseMedia):

    class Meta(BaseMedia.Meta):
        verbose_name = "Model Music"
        verbose_name_plural = "Models of type - Music"

    artist = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(9, message="Artist must be at least 9 characters long")
        ],
    )
