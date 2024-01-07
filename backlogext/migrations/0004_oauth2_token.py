# Generated by Django 3.2.23 on 2024-01-06 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backlogext', '0003_issue_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Oauth2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=255, null=True, verbose_name='code')),
                ('client_id', models.CharField(max_length=255, verbose_name='client id')),
                ('client_secret', models.CharField(max_length=255, verbose_name='client secret')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
            ],
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_token', models.CharField(blank=True, max_length=255, verbose_name='token')),
                ('refresh_token', models.CharField(blank=True, max_length=255, verbose_name='refresh_token')),
                ('expires_in', models.IntegerField(blank=True, verbose_name='expires_in')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
            ],
        ),
    ]
