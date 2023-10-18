# Generated by Django 4.2.3 on 2023-10-18 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserVisit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_identifier', models.CharField(max_length=255)),
                ('ip_address', models.GenericIPAddressField()),
                ('http_method', models.CharField(max_length=10)),
                ('request_url', models.URLField()),
                ('user_agent', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('referred_from', models.URLField(blank=True, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]