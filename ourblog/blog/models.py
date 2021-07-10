from django.db import models

# Create your models here.
class Article(models.Model):
    article_text = models.CharField(max_length=2000)
    pub_date = models.DateTimeField('date published')


class Comment(models.Model):
    comment = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=200)
