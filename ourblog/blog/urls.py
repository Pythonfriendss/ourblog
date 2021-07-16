from django.urls import path

from .views import IndexView, ArticleCreateView, ArticleDetailView, article_post


urlpatterns=[
    path("", IndexView.as_view(), name='index'),
    #path('article/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('<int:pk>/', article_post, name='article-post'),
    path('article/new', ArticleCreateView.as_view(), name='new-article'),
]