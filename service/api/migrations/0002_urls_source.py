# Generated by Django 3.0.2 on 2020-01-20 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='urls',
            name='source',
            field=models.TextField(default='hlzurlbavigation', verbose_name='来源'),
        ),
    ]
