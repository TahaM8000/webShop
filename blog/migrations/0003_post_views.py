# Generated by Django 4.2.3 on 2023-09-13 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_category_options_alter_post_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.PositiveIntegerField(default=0, verbose_name='تعداد بازدید'),
        ),
    ]
