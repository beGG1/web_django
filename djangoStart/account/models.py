from django.db import models
from django.utils.timezone import now
from news.models import Article
from job.models import Job
from django.contrib.auth.models import User
    

# Create your models here.
class Liked_post(models.Model):
    id_user = models.ForeignKey(User, related_name='id_user', on_delete=models.CASCADE)
    id_article = models.ForeignKey(Article, related_name='article', on_delete=models.CASCADE)

class Liked_job(models.Model):
    id_user = models.ForeignKey(User, related_name='id_user_job', on_delete=models.CASCADE)
    id_job = models.ForeignKey(Job, related_name='job', on_delete=models.CASCADE)
