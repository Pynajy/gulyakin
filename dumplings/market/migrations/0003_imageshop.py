# Generated by Django 4.2.5 on 2023-10-02 21:55

from django.db import migrations, models
import django.db.models.deletion
import market.models


class Migration(migrations.Migration):
    dependencies = [
        ("market", "0002_adress_lat_adress_long"),
    ]

    operations = [
        migrations.CreateModel(
            name="ImageShop",
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
                (
                    "image",
                    models.ImageField(
                        upload_to=market.models.shop_image_directory_path
                    ),
                ),
                (
                    "shop",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="market.shop"
                    ),
                ),
            ],
        ),
    ]
