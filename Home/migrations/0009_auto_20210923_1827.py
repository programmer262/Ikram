# Generated by Django 3.2.7 on 2021-09-23 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0008_home_mqs'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Name',
        ),
        migrations.AlterField(
            model_name='home',
            name='mqs',
            field=models.TextField(),
        ),
    ]
