# -*- coding: UTF-8 -*-

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    class Meta:
        db_table = "article"

    article_title = models.CharField(max_length = 200)
    article_taxt = models.TextField()
    article_date = models.DateTimeField()
    article_likes = models.IntegerField(default=0)


class Comments(models.Model):
    class Meta:
        db_table = 'comments'

    comments_text = models.TextField(verbose_name="Текст комментария")
    comments_date = models.DateTimeField(auto_now=True)
    comments_article = models.ForeignKey(Article)
    comments_user = models.ForeignKey(User)
