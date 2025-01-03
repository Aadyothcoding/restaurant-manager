# Generated by Django 5.1.4 on 2024-12-28 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0002_alter_menu_description"),
    ]

    operations = [
        migrations.CreateModel(
            name="Booking",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("phone_number", models.CharField(max_length=15)),
                ("date", models.DateField()),
                ("time", models.TimeField()),
                ("number_of_guests", models.PositiveIntegerField()),
                ("special_requests", models.TextField(blank=True)),
            ],
        ),
    ]
