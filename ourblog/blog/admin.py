from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','author','content',  'status','pub_date')
    list_filter = ("status",)
    search_fields = ['title', 'content']

admin.register(Article, ArticleAdmin)

admin.site.register(Article, ArticleAdmin)
