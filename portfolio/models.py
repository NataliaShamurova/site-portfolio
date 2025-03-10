from django.db import models
from django.urls import reverse


class Author(models.Model):
    name = models.CharField(max_length=15)
    lastname = models.CharField(max_length=15)
    about = models.TextField(blank=True)
    image = models.ImageField(upload_to='resumes')

    class Meta:
        ordering = ['-id']
        verbose_name = 'Резюме'
        verbose_name_plural = 'Резюме'

    def __str__(self):
        return f'{self.name} {self.lastname}'


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    image = models.ImageField(upload_to='project', blank=True, null=True, verbose_name='Изображение')
    stack = models.TextField(blank=True)
    link = models.URLField(max_length=200, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'slug': self.slug})


class Contact(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='contact', blank=True, null=True, verbose_name='Изображение')
    link = models.URLField(max_length=200, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.name
