# Generated by Django 4.2.3 on 2023-09-19 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facades', '0015_banner_arg_banner_main_link_banner_out_link'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cover',
        ),
        migrations.AlterField(
            model_name='banner',
            name='for_what',
            field=models.CharField(choices=[('c2', '2col'), ('c3', '3col'), ('f1', 'fisrt1'), ('f2', 'fisrt2'), ('b1', 'big1')], max_length=2),
        ),
    ]
