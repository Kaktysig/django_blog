from django.db import models
from django.utils import timezone


class Articles(models.Model):
    name = models.CharField(max_length=140)
    content = models.TextField()
    created_at = models.DateField(default=timezone.now)
    comments_on = models.BooleanField(default=True)

    likes = models.IntegerField(default=0)

    user = models.ForeignKey('auth.User', to_field='username')


class Comments(models.Model):
    content = models.TextField()
    created_at = models.DateField(default=timezone.now)
    article_id = models.ForeignKey('blog.Articles', to_field='id')

    user = models.CharField(max_length=140, default='Неизвестный пользователь')