from django.contrib import admin

from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    fields = ['article_text', 'pub_date']

admin.site.register(Article, ArticleAdmin)