# Generated by Django 4.2.3 on 2023-11-12 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facades', '0032_configshop_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='banner',
            name='for_what',
            field=models.CharField(choices=[('c2', '2col'), ('c3', '3col'), ('f1', 'fisrt1'), ('f2', 'fisrt2'), ('b1', 'big1'), ('e1', 'end1'), ('t1', 'category1'), ('t2', 'category2'), ('t3', 'category3'), ('ct', 'category page'), ('ds', 'dashboard'), ('ne', 'news'), ('au', 'aboutUs'), ('ay', 'aboutUsBanner'), ('co', 'contact'), ('fq', 'FAQ'), ('ff', 'full width FAQ'), ('to', 'Track Order'), ('ru', 'Rules')], max_length=2),
        ),
    ]
