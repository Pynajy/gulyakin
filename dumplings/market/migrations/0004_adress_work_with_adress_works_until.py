# Generated by Django 4.2.5 on 2023-10-17 13:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("market", "0003_imageshop"),
    ]

    operations = [
        migrations.AddField(
            model_name="adress",
            name="work_with",
            field=models.TimeField(
                default=datetime.datetime(2023, 10, 17, 16, 19, 14, 858789)
            ),
        ),
        migrations.AddField(
            model_name="adress",
            name="works_until",
            field=models.TimeField(
                default=datetime.datetime(2023, 10, 17, 16, 19, 14, 858789)
            ),
        ),
    ]