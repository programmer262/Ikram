# Generated by Django 3.2.7 on 2021-11-28 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0018_auto_20210926_1604'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='Type',
        ),
        migrations.RemoveField(
            model_name='home',
            name='mqs',
        ),
        migrations.RemoveField(
            model_name='slider',
            name='description',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]
