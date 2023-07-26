# Generated by Django 4.2.3 on 2023-07-21 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stuff', '0008_alter_product_discount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('logo', models.ImageField(upload_to='web_shop/logos/')),
                ('description', models.TextField()),
                ('created', models.DateField(auto_now_add=True)),
            ],
        ),
    ]