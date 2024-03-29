# Generated by Django 4.2.3 on 2023-09-23 02:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0034_rename_articleal_code_address_postal_code'),
        ('orders', '0005_remove_order_address_order_ref_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.address'),
        ),
    ]
