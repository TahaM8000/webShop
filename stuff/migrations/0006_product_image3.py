# Generated by Django 4.2.1 on 2023-05-19 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stuff', '0005_alter_product_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image3',
            field=models.ImageField(default=1, upload_to='web_shop/products/%Y/%m/%d/'),
            preserve_default=False,
        ),
    ]
