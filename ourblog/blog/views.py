<<<<<<< HEAD
<<<<<<< HEAD
from django.shortcuts import render
from django.http import HttpResponse
=======
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
>>>>>>> masterzee
from .models import Article
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

def index(request):
    context = {
        'posts': Article.objects.all()
    }
<<<<<<< HEAD
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
=======
    return render(request, 'index.html', context)

class IndexView(ListView):
    model = Article
    context_object_name = 'article'
    template_name = 'index.html'
    ordering = ['-pub_date']
    paginate_by = 5

    # def get_queryset(self):
    #     user = get_object_or_404(User, username=self.kwargs.get('username'))
    #     return Article.objects.filter(author=user).order_by('-date_posted')

    # def get_queryset(self):
    #     return Article.objects.order_by('-pub_date')[:10]
    
class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article-detail.html'

class ArticleCreateView(CreateView):
    model = Article
    fields = ['title', 'content']
>>>>>>> masterzee
