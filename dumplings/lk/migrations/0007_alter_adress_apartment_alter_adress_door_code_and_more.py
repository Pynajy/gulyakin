# Generated by Django 4.2.5 on 2023-10-29 06:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("lk", "0006_adress_apartment_adress_door_code_adress_entrance_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="adress",
            name="apartment",
            field=models.IntegerField(blank=True, default="0"),
        ),
        migrations.AlterField(
            model_name="adress",
            name="door_code",
            field=models.IntegerField(blank=True, default="0"),
        ),
        migrations.AlterField(
            model_name="adress",
            name="entrance",
            field=models.IntegerField(blank=True, default="0"),
        ),
        migrations.AlterField(
            model_name="adress",
            name="floor",
            field=models.IntegerField(blank=True, default="0"),
        ),
    ]
