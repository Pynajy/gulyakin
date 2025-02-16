# Generated by Django 4.2.5 on 2023-10-17 12:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0003_alter_userorderhystory_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="DeliveryType",
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
                ("title", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="PymentType",
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
                ("title", models.CharField(max_length=100)),
                ("is_payment", models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name="userorderhystory",
            name="is_call",
            field=models.BooleanField(default=True),
        ),
    ]
