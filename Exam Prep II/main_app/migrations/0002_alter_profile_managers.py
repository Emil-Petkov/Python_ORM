# Generated by Django 4.2.7 on 2023-11-24 14:24

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='profile',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]