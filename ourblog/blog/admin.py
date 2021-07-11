from django.contrib import admin
from .models import Article, Comment


<<<<<<< HEAD
# Register your models here.
admin.site.register(Article)
admin.site.register(Comment)
=======
from .models import Article, Comment

class ArticleAdmin(admin.ModelAdmin):
    fields = ['title_text', 'article_text', 'pub_date', 'author']

class CommentAdmin(admin.ModelAdmin):
    fields = ['comment', 'comment_text', 'pub_date', 'author']

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
>>>>>>> 7531963e5667724879b77948df21733b641b9b63
