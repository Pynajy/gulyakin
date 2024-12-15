# Generated by Django 4.2.5 on 2023-10-18 09:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("market", "0005_alter_adress_work_with_alter_adress_works_until_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="TimeZone",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name="adress",
            name="work_with",
            field=models.TimeField(
                default=datetime.datetime(2023, 10, 18, 12, 8, 59, 481872)
            ),
        ),
        migrations.AlterField(
            model_name="adress",
            name="works_until",
            field=models.TimeField(
                default=datetime.datetime(2023, 10, 18, 12, 8, 59, 481872)
            ),
        ),
    ]
