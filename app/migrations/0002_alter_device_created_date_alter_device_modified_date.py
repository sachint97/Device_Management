# Generated by Django 4.2.3 on 2023-07-18 13:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="device",
            name="created_date",
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="device",
            name="modified_date",
            field=models.DateField(),
        ),
    ]
