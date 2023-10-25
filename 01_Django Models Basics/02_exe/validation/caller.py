import os
import django
from django.core.exceptions import ValidationError

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here

# Create queries within functions

from main_app.models import TestPerson

try:
    invalid_person = TestPerson(
        name='Ivan',
        age=121,
    )
    invalid_person.full_clean()
except ValidationError as e:
    print(e)
