# Generated by Django 3.2.7 on 2021-09-24 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0011_home_slider'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(height_field=600, upload_to='sliders/', width_field=500)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='home',
            name='mqs',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='home',
            name='slider',
            field=models.TextField(blank=True, null=True),
        ),
    ]
