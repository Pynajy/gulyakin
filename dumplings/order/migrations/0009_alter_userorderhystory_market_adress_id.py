# Generated by Django 4.2.5 on 2023-10-19 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("market", "0018_alter_adress_work_with_alter_adress_works_until"),
        ("order", "0008_userorderhystory_market_adress_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userorderhystory",
            name="market_adress_id",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="market.adress",
            ),
        ),
    ]
