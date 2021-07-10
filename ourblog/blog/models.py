from django.db import models
from django.utils import timezone
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=150)
    article_text = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)


class Comment(models.Model):
    comment = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=200)
