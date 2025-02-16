# Generated by Django 5.0 on 2023-12-13 17:44

import datetime
import django.db.models.deletion
import market.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0064_alter_adress_friday_until_alter_adress_friday_with_and_more'),
        ('product', '0021_products_is_multiple_supplements'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adress',
            options={'verbose_name_plural': 'Адреса магазинов'},
        ),
        migrations.AlterModelOptions(
            name='imageshop',
            options={'verbose_name_plural': 'Фотографии магазинов'},
        ),
        migrations.AlterModelOptions(
            name='shop',
            options={'verbose_name_plural': 'Магазины'},
        ),
        migrations.AlterModelOptions(
            name='siti',
            options={'verbose_name_plural': 'Города'},
        ),
        migrations.AlterModelOptions(
            name='timezone',
            options={'verbose_name_plural': 'Часовые пояса'},
        ),
        migrations.AlterField(
            model_name='adress',
            name='adress',
            field=models.CharField(max_length=500, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='adress',
            name='friday_until',
            field=models.TimeField(default=datetime.datetime(2023, 12, 13, 20, 44, 15, 121902), verbose_name='Пятница до'),
        ),
        migrations.AlterField(
            model_name='adress',
            name='friday_with',
            field=models.TimeField(default=datetime.datetime(2023, 12, 13, 20, 44, 15, 121902), verbose_name='Пятница с'),
        ),
        migrations.AlterField(
            model_name='adress',
            name='is_around_clock',
            field=models.BooleanField(default=False, verbose_name='Круглосуточно?'),
        ),
        migrations.AlterField(
            model_name='adress',
            name='lat',
            field=models.FloatField(default=0.0, verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='adress',
            name='long',
            field=models.FloatField(default=0.0, verbose_name='Долгота'),
        ),
        migrations.AlterField(
            model_name='adress',
            name='monday_until',
            field=models.TimeField(default=datetime.datetime(2023, 12, 13, 20, 44, 15, 121902), verbose_name='Понедельник до'),
        ),
        migrations.AlterField(
            model_name='adress',
            name='monday_with',
            field=models.TimeField(default=datetime.datetime(2023, 12, 13, 20, 44, 15, 121902), verbose_name='Понедельник с'),
        ),
        migrations.AlterField(
            model_name='adress',
            name='phone',
            field=models.CharField(default=79991112233, max_length=15, verbose_name='Телефон для связи'),
        ),
        migrations.AlterField(
            model_name='adress',
            name='saturday_until',
            field=models.TimeField(default=datetime.datetime(2023, 12, 13, 20, 44, 15, 121902), verbose_name='Суббота до'),
        ),
        migrations.AlterField(
            model_name='adress',
            name='saturday_with',
            field=models.TimeField(default=datetime.datetime(2023, 12, 13, 20, 44, 15, 121902), verbose_name='Суббота с'),
        ),
        migrations.AlterField(
            model_name='adress',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.shop', verbose_name='Магазин'),
        ),
        migrations.AlterField(
            model_name='adress',
            name='siti',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.siti', verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='adress',
            name='sunday_until',
            field=models.TimeField(default=datetime.datetime(2023, 12, 13, 20, 44, 15, 121902), verbose_name='Воскресенье до'),
        ),
        migrations.AlterField(
            model_name='adress',
            name='sunday_with',
            field=models.TimeField(default=datetime.datetime(2023, 12, 13, 20, 44, 15, 121902), verbose_name='Воскресенье с'),
        ),
        migrations.AlterField(
            model_name='adress',
            name='thursday_until',
            field=models.TimeField(default=datetime.datetime(2023, 12, 13, 20, 44, 15, 121902), verbose_name='Четверг до'),
        ),
        migrations.AlterField(
            model_name='adress',
            name='thursday_with',
            field=models.TimeField(default=datetime.datetime(2023, 12, 13, 20, 44, 15, 121902), verbose_name='Четвер с'),
        ),
        migrations.AlterField(
            model_name='adress',
            name='timezone',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='market.timezone', verbose_name='Часовая зона'),
        ),
        migrations.AlterField(
            model_name='adress',
            name='tuesday_until',
            field=models.TimeField(default=datetime.datetime(2023, 12, 13, 20, 44, 15, 121902), verbose_name='Вторник до'),
        ),
        migrations.AlterField(
            model_name='adress',
            name='tuesday_with',
            field=models.TimeField(default=datetime.datetime(2023, 12, 13, 20, 44, 15, 121902), verbose_name='Вторник с'),
        ),
        migrations.AlterField(
            model_name='adress',
            name='wednesday_until',
            field=models.TimeField(default=datetime.datetime(2023, 12, 13, 20, 44, 15, 121902), verbose_name='Среда до'),
        ),
        migrations.AlterField(
            model_name='adress',
            name='wednesday_with',
            field=models.TimeField(default=datetime.datetime(2023, 12, 13, 20, 44, 15, 121902), verbose_name='Среда с'),
        ),
        migrations.AlterField(
            model_name='imageshop',
            name='image',
            field=models.ImageField(upload_to=market.models.shop_image_directory_path, verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='imageshop',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.adress', verbose_name='Магазин'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='combo',
            field=models.ManyToManyField(blank=True, to='product.combo', verbose_name='Комбо'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='description',
            field=models.TextField(blank=True, verbose_name='Полное описание'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='link',
            field=models.IntegerField(default=1, verbose_name='Внутренний номер'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='products',
            field=models.ManyToManyField(blank=True, to='product.products', verbose_name='Продукты'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='short_description',
            field=models.CharField(blank=True, max_length=500, verbose_name='Короткое описание'),
        ),
        migrations.AlterField(
            model_name='siti',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Название города'),
        ),
        migrations.AlterField(
            model_name='timezone',
            name='title',
            field=models.CharField(max_length=500, verbose_name='Часовая зона(+2)'),
        ),
    ]
