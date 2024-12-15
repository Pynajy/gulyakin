# Generated by Django 4.2.5 on 2023-10-18 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("market", "0013_alter_adress_work_with_alter_adress_works_until"),
        ("product", "0005_dayweek"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProductDay",
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
                    "day_week",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="product.dayweek",
                    ),
                ),
                (
                    "market",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="market.shop"
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="product.products",
                    ),
                ),
            ],
        ),
    ]
