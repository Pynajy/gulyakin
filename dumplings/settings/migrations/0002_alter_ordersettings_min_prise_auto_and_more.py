# Generated by Django 4.2.5 on 2023-10-17 12:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("settings", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ordersettings",
            name="min_prise_auto",
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name="ordersettings",
            name="min_prise_people",
            field=models.FloatField(),
        ),
    ]
