# Generated by Django 4.2.3 on 2023-10-10 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facades', '0021_alter_banner_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='phoneNumber',
            field=models.CharField(default='None', max_length=200),
        ),
        migrations.AlterField(
            model_name='survey',
            name='text',
            field=models.TextField(default='None'),
        ),
    ]