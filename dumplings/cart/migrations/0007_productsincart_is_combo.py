# Generated by Django 4.2.5 on 2023-10-30 17:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cart", "0006_remove_comboincart_count"),
    ]

    operations = [
        migrations.AddField(
            model_name="productsincart",
            name="is_combo",
            field=models.BooleanField(default=False),
        ),
    ]
