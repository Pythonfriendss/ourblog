from django.contrib import admin
from .models import Article, Comment


# Register your models here.
admin.site.register(Article)
admin.site.register(Comment)
from .models import Article, Comment

class ArticleAdmin(admin.ModelAdmin):
    fields = ['title_text', 'article_text', 'pub_date', 'author']

class CommentAdmin(admin.ModelAdmin):
    fields = ['comment', 'comment_text', 'pub_date', 'author']

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
