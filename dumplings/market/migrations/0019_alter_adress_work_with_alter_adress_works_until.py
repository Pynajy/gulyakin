# Generated by Django 4.2.5 on 2023-10-22 19:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("market", "0018_alter_adress_work_with_alter_adress_works_until"),
    ]

    operations = [
        migrations.AlterField(
            model_name="adress",
            name="work_with",
            field=models.TimeField(
                default=datetime.datetime(2023, 10, 22, 22, 50, 45, 198653)
            ),
        ),
        migrations.AlterField(
            model_name="adress",
            name="works_until",
            field=models.TimeField(
                default=datetime.datetime(2023, 10, 22, 22, 50, 45, 198653)
            ),
        ),
    ]
