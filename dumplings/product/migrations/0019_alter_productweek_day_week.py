# Generated by Django 4.2.5 on 2023-11-15 23:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0018_numberweek_productweek"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productweek",
            name="day_week",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="product.numberweek"
            ),
        ),
    ]
