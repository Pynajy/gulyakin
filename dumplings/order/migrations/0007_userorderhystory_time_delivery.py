# Generated by Django 4.2.5 on 2023-10-18 21:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0006_userorderhystory_pyment_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="userorderhystory",
            name="time_delivery",
            field=models.CharField(blank=True, default="None", max_length=50),
        ),
    ]