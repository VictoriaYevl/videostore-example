# Generated by Django 3.2.3 on 2021-06-02 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20191112_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
