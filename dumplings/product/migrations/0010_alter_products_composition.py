# Generated by Django 4.2.5 on 2023-10-23 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0009_alter_category_image_alter_combo_image_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="products",
            name="composition",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="product.composition",
            ),
        ),
    ]