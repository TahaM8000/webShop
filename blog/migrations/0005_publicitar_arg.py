# Generated by Django 4.2.3 on 2023-09-15 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_publicitar'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicitar',
            name='arg',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
