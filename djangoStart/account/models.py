from django.db import models
from django.utils.timezone import now
from news.models import Article
from django.contrib.auth.models import User

# Create your models here.
class Liked_post(models.Model):
    id_user = models.ForeignKey(User, related_name='id_user', on_delete=models.CASCADE)
    id_article = models.ForeignKey(Article, related_name='article', on_delete=models.CASCADE)

    def __str__(self):
        return self.title