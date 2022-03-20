from django.db import models

# Create your models here.
class Job(models.Model):
    title = models.CharField('Название', max_length=50, default='')
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статья')

    def __str__(self):
        return self.title