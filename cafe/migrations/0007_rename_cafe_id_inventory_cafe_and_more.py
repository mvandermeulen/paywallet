# Generated by Django 4.2.5 on 2023-11-18 16:46

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("cafe", "0006_alter_order_options"),
    ]

    operations = [
        migrations.RenameField(
            model_name="inventory",
            old_name="cafe_id",
            new_name="cafe",
        ),
        migrations.RenameField(
            model_name="inventory",
            old_name="product_id",
            new_name="product",
        ),
    ]
