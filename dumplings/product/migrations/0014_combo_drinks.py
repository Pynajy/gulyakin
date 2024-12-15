# Generated by Django 4.2.5 on 2023-10-29 16:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0013_products_base_supplements_products_is_supplement"),
    ]

    operations = [
        migrations.AddField(
            model_name="combo",
            name="drinks",
            field=models.ManyToManyField(
                blank=True, related_name="drinks", to="product.products"
            ),
        ),
    ]