from django.urls import path

from .views import IndexView, ArticleCreateView, ArticleDetailView


urlpatterns=[
    path("", IndexView.as_view(), name='index'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('article/new', ArticleCreateView.as_view(), name='new-article'),
]