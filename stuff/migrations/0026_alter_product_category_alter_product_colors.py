# Generated by Django 4.2.3 on 2023-10-14 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stuff', '0025_alter_product_brand_alter_product_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(blank=True, related_name='products', to='stuff.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='colors',
            field=models.ManyToManyField(blank=True, to='stuff.color'),
        ),
    ]
