from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    image = models.FilePathField(path="/images", default=None)
    content = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    status = models.IntegerField(choices=STATUS, default=0)
    
class Comment(models.Model):
    post = models.ForeignKey(Article,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"