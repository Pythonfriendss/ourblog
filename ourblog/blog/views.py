from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .forms import CommentForm
from .models import Article, Comment
from django.views.generic import ListView, DetailView, CreateView

def index(request):
    context = {
        'articles': Article.objects.all()
    }
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

def article_post(request, pk):
    template_name = 'article-detail.html'
    article = get_object_or_404(Article, pk=pk)
    comments = article.comments.filter(active=True).order_by("-created_on")
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = article
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'article': article,
                                        'comments': comments,
                                        'new_comment': new_comment,
                                        'comment_form': comment_form})

class ArticleCreateView(CreateView):
    model = Article
    fields = ['title', 'content']