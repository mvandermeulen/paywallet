# Generated by Django 4.2.5 on 2024-03-11 08:50

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("cafe", "0006_alter_cafe_admin"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="vendoradmin",
            name="cafe",
        ),
    ]