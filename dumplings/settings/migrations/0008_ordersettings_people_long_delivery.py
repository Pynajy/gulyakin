# Generated by Django 4.2.5 on 2023-10-27 13:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("settings", "0007_alter_telegarambotforadressmarket_chanel"),
    ]

    operations = [
        migrations.AddField(
            model_name="ordersettings",
            name="people_long_delivery",
            field=models.IntegerField(default=1500),
        ),
    ]