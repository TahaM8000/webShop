# Generated by Django 4.2.3 on 2023-10-19 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stuff', '0029_product_transit_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='slug',
            field=models.SlugField(allow_unicode=True, max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(allow_unicode=True, max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(allow_unicode=True, max_length=200, unique=True),
        ),
    ]
