# Generated by Django 4.2.5 on 2023-10-28 18:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("lk", "0003_adress_is_activ"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="dob",
            field=models.CharField(blank=True, default="", max_length=10),
        ),
    ]