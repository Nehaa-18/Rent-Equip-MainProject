# Generated by Django 4.1.5 on 2023-11-26 14:54

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0012_product_company"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="company",
        ),
    ]
