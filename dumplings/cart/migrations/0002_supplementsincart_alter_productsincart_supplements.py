# Generated by Django 4.2.5 on 2023-10-18 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0003_alter_category_image"),
        ("cart", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="SupplementsInCart",
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
                ("count", models.IntegerField()),
                (
                    "supplements",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="product.supplements",
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="productsincart",
            name="supplements",
            field=models.ManyToManyField(to="cart.supplementsincart"),
        ),
    ]