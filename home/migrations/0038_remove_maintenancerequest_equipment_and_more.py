# Generated by Django 4.1.5 on 2024-04-05 06:17

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0037_review_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="maintenancerequest",
            name="equipment",
        ),
        migrations.RemoveField(
            model_name="maintenancerequest",
            name="user",
        ),
        migrations.DeleteModel(
            name="ProductBooking",
        ),
        migrations.DeleteModel(
            name="MaintenanceRequest",
        ),
    ]