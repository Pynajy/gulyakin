# Generated by Django 4.2.5 on 2023-11-15 07:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("market", "0052_alter_adress_work_with_alter_adress_works_until"),
    ]

    operations = [
        migrations.AlterField(
            model_name="adress",
            name="work_with",
            field=models.TimeField(
                default=datetime.datetime(2023, 11, 15, 10, 50, 35, 313369)
            ),
        ),
        migrations.AlterField(
            model_name="adress",
            name="works_until",
            field=models.TimeField(
                default=datetime.datetime(2023, 11, 15, 10, 50, 35, 313369)
            ),
        ),
    ]
