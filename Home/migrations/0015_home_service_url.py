# Generated by Django 3.2.7 on 2021-09-24 23:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0014_home_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='home_service',
            name='url',
            field=models.URLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
