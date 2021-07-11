<<<<<<< HEAD
from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

def index(request):
    context = {
        'posts': Article.objects.all()
    }
    return HttpResponse("Hello, world. You're at the pblog index page.")
=======
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Article, Comment
from django.urls import reverse
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'blog/index.html'

    def get_queryset(self):
        return Article.objects.order_by('-pub_date')[:10]

class ArticleView(generic.DetailView):
    template_name = 'blog/detail.html'
    model = Article
    
>>>>>>> 7531963e5667724879b77948df21733b641b9b63
