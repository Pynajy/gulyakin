# Generated by Django 4.2.5 on 2023-10-03 08:46

from django.db import migrations, models
import product.models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0002_products_weight"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="image",
            field=models.ImageField(
                default="None", upload_to=product.models.category_image_directory_path
            ),
        ),
    ]
