# Generated by Django 5.0 on 2023-12-15 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0014_userorderhystory_count_tools'),
    ]

    operations = [
        migrations.AddField(
            model_name='userorderhystory',
            name='discount',
            field=models.IntegerField(default=0),
        ),
    ]
