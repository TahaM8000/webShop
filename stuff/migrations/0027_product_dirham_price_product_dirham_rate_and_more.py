# Generated by Django 4.2.3 on 2023-10-18 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stuff', '0026_alter_product_category_alter_product_colors'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='dirham_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='dirham_rate',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='height',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='length',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_barcode',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='weight',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='width',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
