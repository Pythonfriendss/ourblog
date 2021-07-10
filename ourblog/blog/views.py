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