# Generated by Django 5.0 on 2023-12-24 08:49

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="price",
            new_name="unit_price",
        ),
    ]
