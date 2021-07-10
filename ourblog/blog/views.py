from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Article, Comment
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView


class IndexView(ListView):
    model = Article
    context_object_name = 'article'
    template_name = 'blog/index.html'

    def get_queryset(self):
        return Article.objects.order_by('-pub_date')[:10]
    
class ArticleDetailView(DetailView):
    model = Article

class ArticleCreateView(CreateView):
    model = Article
    fields = ['title', 'content']