# Generated by Django 4.2.5 on 2023-10-02 21:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("market", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="adress",
            name="lat",
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name="adress",
            name="long",
            field=models.FloatField(default=0.0),
        ),
    ]
