# Generated by Django 4.2.3 on 2023-09-22 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0033_alter_address_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='articleal_code',
            new_name='postal_code',
        ),
    ]
