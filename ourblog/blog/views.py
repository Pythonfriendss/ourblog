from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Article, Comment
from django.urls import reverse
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'blog/index.html'