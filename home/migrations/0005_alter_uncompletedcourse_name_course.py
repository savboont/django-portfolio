# Generated by Django 4.1.1 on 2022-09-22 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_completedcourse_uncompletedcourse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uncompletedcourse',
            name='name_course',
            field=models.TextField(),
        ),
    ]
