# Generated by Django 4.2.3 on 2023-09-20 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facades', '0017_delete_endbanner_banner_button_alter_banner_for_what'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='for_what',
            field=models.CharField(choices=[('c2', '2col'), ('c3', '3col'), ('f1', 'fisrt1'), ('f2', 'fisrt2'), ('b1', 'big1'), ('e1', 'end1'), ('t1', 'category1'), ('t2', 'category2'), ('t3', 'category3'), ('t4', 'category4')], max_length=2),
        ),
    ]
