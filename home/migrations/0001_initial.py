# Generated by Django 4.1.1 on 2022-09-20 15:18

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proj_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('proj_link', models.CharField(max_length=100)),
                ('images', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('telegram', models.CharField(max_length=100)),
                ('hhru', models.CharField(max_length=100)),
            ],
        ),
    ]