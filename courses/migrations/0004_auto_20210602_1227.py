# Generated by Django 3.2.3 on 2021-06-02 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_course_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(verbose_name='Введите описание курса'),
        ),
        migrations.AlterField(
            model_name='course',
            name='img',
            field=models.ImageField(default='default.png', upload_to='course_images', verbose_name='Загрузить фото'),
        ),
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.SlugField(max_length=100, unique=True, verbose_name='Название URL*'),
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(max_length=120, verbose_name='Название курса*'),
        ),
    ]
