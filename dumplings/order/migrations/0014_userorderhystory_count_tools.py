# Generated by Django 5.0 on 2023-12-13 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0013_alter_deliverytype_options_alter_pymenttype_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userorderhystory',
            name='count_tools',
            field=models.IntegerField(default=1),
        ),
    ]