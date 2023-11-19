# Generated by Django 4.2.7 on 2023-11-19 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_owner_car'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_number', models.CharField(max_length=10, unique=True)),
                ('registration_date', models.DateField(blank=True, null=True)),
                ('car', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.car')),
            ],
        ),
    ]
