# Generated by Django 4.2.5 on 2023-10-23 10:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("market", "0024_alter_adress_work_with_alter_adress_works_until_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="adress",
            name="work_with",
            field=models.TimeField(
                default=datetime.datetime(2023, 10, 23, 13, 11, 41, 657974)
            ),
        ),
        migrations.AlterField(
            model_name="adress",
            name="works_until",
            field=models.TimeField(
                default=datetime.datetime(2023, 10, 23, 13, 11, 41, 662990)
            ),
        ),
    ]