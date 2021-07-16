from django.contrib import admin
from .models import Article, Comment


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','author','content',  'status','pub_date')
    list_filter = ("status",)
    search_fields = ['title', 'content']

admin.register(Article, ArticleAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
