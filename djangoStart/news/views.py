from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DeleteView
from django.contrib import messages
from .models import Article, Comment
from .forms import CommentForm
from django.contrib.auth.models import User
from account.models import Liked_post
from django.urls import reverse_lazy

# Create your views here.
def news_home(request):
    news = Article.objects.all()
    return render(request, 'news/news_home.html', {'news': news})


'''class NewsDetailView(DeleteView):
    model = Article
    template_name = 'news/detail_view.html'
    context_object_name = 'article'''
 

def news_detail(request, pk):
    form = CommentForm()
    news = get_object_or_404(Article, id=pk)
    comments = Comment.objects.filter(post=pk)
    like = Liked_post()

    if request.method == 'LIKE':
        like.id_article = news
        like.id_user = request.user
        like.save()

    if request.method == 'POST':
        f = CommentForm(request.POST)
        if f.is_valid():
            comm = f.save(commit=False)
            comm.post = news
            comm.save()
    return render(request, 'news/detail_view.html', {'article': news, 'comments': comments, 'form': form})

'''def like(request):
    #like = Liked_post()
    #like.id_article = article
    #like.id_user = request.user
    #like.save()
    return reverse_lazy('news/detail_view.html')'''