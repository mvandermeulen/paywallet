# Generated by Django 4.2.5 on 2024-03-08 05:18

from django.db import migrations, models
import paywallet.storage_backends


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(
                blank=True,
                storage=paywallet.storage_backends.PublicMediaStorage(),
                upload_to="products/",
            ),
        ),
    ]
