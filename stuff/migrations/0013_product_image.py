# Generated by Django 4.2.3 on 2023-07-31 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stuff', '0012_remove_product_images_productimage_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=1, upload_to='web_shop/products/%Y/%m/%d/'),
            preserve_default=False,
        ),
    ]