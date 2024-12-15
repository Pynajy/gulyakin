# Generated by Django 4.2.5 on 2023-11-18 14:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("market", "0062_remove_adress_work_with_remove_adress_works_until_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="adress",
            name="friday",
        ),
        migrations.RemoveField(
            model_name="adress",
            name="monday",
        ),
        migrations.RemoveField(
            model_name="adress",
            name="saturday",
        ),
        migrations.RemoveField(
            model_name="adress",
            name="sunday",
        ),
        migrations.RemoveField(
            model_name="adress",
            name="thursday",
        ),
        migrations.RemoveField(
            model_name="adress",
            name="tuesday",
        ),
        migrations.RemoveField(
            model_name="adress",
            name="wednesday",
        ),
        migrations.AddField(
            model_name="adress",
            name="friday_until",
            field=models.TimeField(
                default=datetime.datetime(2023, 11, 18, 17, 59, 18, 218487)
            ),
        ),
        migrations.AddField(
            model_name="adress",
            name="friday_with",
            field=models.TimeField(
                default=datetime.datetime(2023, 11, 18, 17, 59, 18, 218487)
            ),
        ),
        migrations.AddField(
            model_name="adress",
            name="monday_until",
            field=models.TimeField(
                default=datetime.datetime(2023, 11, 18, 17, 59, 18, 218487)
            ),
        ),
        migrations.AddField(
            model_name="adress",
            name="monday_with",
            field=models.TimeField(
                default=datetime.datetime(2023, 11, 18, 17, 59, 18, 218487)
            ),
        ),
        migrations.AddField(
            model_name="adress",
            name="saturday_until",
            field=models.TimeField(
                default=datetime.datetime(2023, 11, 18, 17, 59, 18, 218487)
            ),
        ),
        migrations.AddField(
            model_name="adress",
            name="saturday_with",
            field=models.TimeField(
                default=datetime.datetime(2023, 11, 18, 17, 59, 18, 218487)
            ),
        ),
        migrations.AddField(
            model_name="adress",
            name="sunday_until",
            field=models.TimeField(
                default=datetime.datetime(2023, 11, 18, 17, 59, 18, 218487)
            ),
        ),
        migrations.AddField(
            model_name="adress",
            name="sunday_with",
            field=models.TimeField(
                default=datetime.datetime(2023, 11, 18, 17, 59, 18, 218487)
            ),
        ),
        migrations.AddField(
            model_name="adress",
            name="thursday_until",
            field=models.TimeField(
                default=datetime.datetime(2023, 11, 18, 17, 59, 18, 218487)
            ),
        ),
        migrations.AddField(
            model_name="adress",
            name="thursday_with",
            field=models.TimeField(
                default=datetime.datetime(2023, 11, 18, 17, 59, 18, 218487)
            ),
        ),
        migrations.AddField(
            model_name="adress",
            name="tuesday_until",
            field=models.TimeField(
                default=datetime.datetime(2023, 11, 18, 17, 59, 18, 218487)
            ),
        ),
        migrations.AddField(
            model_name="adress",
            name="tuesday_with",
            field=models.TimeField(
                default=datetime.datetime(2023, 11, 18, 17, 59, 18, 218487)
            ),
        ),
        migrations.AddField(
            model_name="adress",
            name="wednesday_until",
            field=models.TimeField(
                default=datetime.datetime(2023, 11, 18, 17, 59, 18, 218487)
            ),
        ),
        migrations.AddField(
            model_name="adress",
            name="wednesday_with",
            field=models.TimeField(
                default=datetime.datetime(2023, 11, 18, 17, 59, 18, 218487)
            ),
        ),
    ]
