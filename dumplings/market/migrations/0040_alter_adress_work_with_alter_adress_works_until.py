# Generated by Django 4.2.5 on 2023-10-30 17:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("market", "0039_alter_adress_work_with_alter_adress_works_until"),
    ]

    operations = [
        migrations.AlterField(
            model_name="adress",
            name="work_with",
            field=models.TimeField(
                default=datetime.datetime(2023, 10, 30, 20, 38, 8, 257308)
            ),
        ),
        migrations.AlterField(
            model_name="adress",
            name="works_until",
            field=models.TimeField(
                default=datetime.datetime(2023, 10, 30, 20, 38, 8, 257308)
            ),
        ),
    ]
