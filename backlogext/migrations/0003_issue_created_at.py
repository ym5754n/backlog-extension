# Generated by Django 3.2.23 on 2024-01-06 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backlogext', '0002_issue_key_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='created_at',
            field=models.DateTimeField(auto_now=True, verbose_name='作成日時'),
        ),
    ]
