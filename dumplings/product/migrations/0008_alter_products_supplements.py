# Generated by Django 4.2.5 on 2023-10-22 19:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0007_dayweek_number_day"),
    ]

    operations = [
        migrations.AlterField(
            model_name="products",
            name="supplements",
            field=models.ManyToManyField(blank=True, to="product.supplements"),
        ),
    ]