# Generated by Django 4.1.5 on 2024-02-12 04:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0020_rename_driver_d_driver_driver_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="Technician",
            fields=[
                ("tech_id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("phone_number", models.CharField(max_length=15)),
                ("expertise", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("address", models.TextField()),
            ],
        ),
    ]
