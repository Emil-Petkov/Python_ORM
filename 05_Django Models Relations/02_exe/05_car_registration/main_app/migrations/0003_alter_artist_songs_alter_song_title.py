# Generated by Django 4.2.7 on 2023-11-18 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_song_artist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='songs',
            field=models.ManyToManyField(related_name='artists', to='main_app.song'),
        ),
        migrations.AlterField(
            model_name='song',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
