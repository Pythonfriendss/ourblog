from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Article(models.Model):
    title_text = models.CharField(max_length=200)
    article_text = models.CharField(max_length=2000)
    pub_date = models.DateTimeField('date published')
    author = CharField(max_length=20)


class Comment(models.Model):
    comment = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
