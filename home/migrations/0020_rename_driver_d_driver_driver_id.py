# Generated by Django 4.1.5 on 2024-02-09 06:49

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0019_driver"),
    ]

    operations = [
        migrations.RenameField(
            model_name="driver",
            old_name="driver_d",
            new_name="driver_id",
        ),
    ]
