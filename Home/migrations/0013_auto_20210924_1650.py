# Generated by Django 3.2.7 on 2021-09-24 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0012_auto_20210924_0121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=300)),
                ('Last_name', models.CharField(max_length=300)),
                ('Tel', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=100)),
                ('Message', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='slider',
            name='image',
            field=models.ImageField(upload_to='sliders/'),
        ),
    ]
