# Generated by Django 3.2.7 on 2021-09-23 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0006_service_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jo', models.CharField(max_length=50)),
            ],
        ),
    ]