# Generated by Django 4.2.3 on 2023-09-18 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facades', '0012_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='for_what',
            field=models.CharField(choices=[('2c', '2col'), ('3c', '3col')], max_length=2),
        ),
    ]