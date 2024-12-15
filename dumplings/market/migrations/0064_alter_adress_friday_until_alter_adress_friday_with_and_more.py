# Generated by Django 4.2.5 on 2023-11-18 15:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("market", "0063_remove_adress_friday_remove_adress_monday_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="adress",
            name="friday_until",
            field=models.TimeField(
                default=datetime.datetime(2023, 11, 18, 18, 59, 55, 440170)
            ),
        ),
        migrations.AlterField(
            model_name="adress",
            name="friday_with",
            field=models.TimeField(
                default=datetime.datetime(2023, 11, 18, 18, 59, 55, 440170)
            ),
        ),
        migrations.AlterField(
            model_name="adress",
            name="monday_until",
            field=models.TimeField(
                default=datetime.datetime(2023, 11, 18, 18, 59, 55, 440170)
            ),
        ),
        migrations.AlterField(
            model_name="adress",
            name="monday_with",
            field=models.TimeField(
                default=datetime.datetime(2023, 11, 18, 18, 59, 55, 440170)
            ),
        ),
        migrations.AlterField(
            model_name="adress",
            name="saturday_until",
            field=models.TimeField(
                default=datetime.datetime(2023, 11, 18, 18, 59, 55, 440170)
            ),
        ),
        migrations.AlterField(
            model_name="adress",
            name="saturday_with",
            field=models.TimeField(
                default=datetime.datetime(2023, 11, 18, 18, 59, 55, 440170)
            ),
        ),
        migrations.AlterField(
            model_name="adress",
            name="sunday_until",
            field=models.TimeField(
                default=datetime.datetime(2023, 11, 18, 18, 59, 55, 440170)
            ),
        ),
        migrations.AlterField(
            model_name="adress",
            name="sunday_with",
            field=models.TimeField(
                default=datetime.datetime(2023, 11, 18, 18, 59, 55, 440170)
            ),
        ),
        migrations.AlterField(
            model_name="adress",
            name="thursday_until",
            field=models.TimeField(
                default=datetime.datetime(2023, 11, 18, 18, 59, 55, 440170)
            ),
        ),
        migrations.AlterField(
            model_name="adress",
            name="thursday_with",
            field=models.TimeField(
                default=datetime.datetime(2023, 11, 18, 18, 59, 55, 440170)
            ),
        ),
        migrations.AlterField(
            model_name="adress",
            name="tuesday_until",
            field=models.TimeField(
                default=datetime.datetime(2023, 11, 18, 18, 59, 55, 440170)
            ),
        ),
        migrations.AlterField(
            model_name="adress",
            name="tuesday_with",
            field=models.TimeField(
                default=datetime.datetime(2023, 11, 18, 18, 59, 55, 440170)
            ),
        ),
        migrations.AlterField(
            model_name="adress",
            name="wednesday_until",
            field=models.TimeField(
                default=datetime.datetime(2023, 11, 18, 18, 59, 55, 440170)
            ),
        ),
        migrations.AlterField(
            model_name="adress",
            name="wednesday_with",
            field=models.TimeField(
                default=datetime.datetime(2023, 11, 18, 18, 59, 55, 440170)
            ),
        ),
    ]