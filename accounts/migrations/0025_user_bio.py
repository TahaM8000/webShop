# Generated by Django 4.2.3 on 2023-09-10 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0024_user_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
