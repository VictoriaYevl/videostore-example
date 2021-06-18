from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Course(models.Model):
    slug = models.SlugField('Название URL', max_length=100, unique=True) # Для создания своего URL адреса
    title = models.CharField('Название курса', max_length=120)
    description = models.TextField('Введите описание курса')
    img = models.ImageField('Загрузить фото', default='default.png', upload_to='course_images')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('course-detail', kwargs={'slug': self.slug})



class Lesson(models.Model):
    slug = models.SlugField()  # Для создания своего URL адреса
    title = models.CharField(max_length=120)
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    number = models.IntegerField()
    video_url = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('lesson-detail', kwargs={'slug': self.course.slug, 'lesson_slug': self.slug})
