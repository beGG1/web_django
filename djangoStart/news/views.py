from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DeleteView
from django.contrib import messages
from .models import Article, Comment
from .forms import CommentForm

# Create your views here.
def news_home(request):
    news = Article.objects.all()
    return render(request, 'news/news_home.html', {'news': news})


class NewsDetailView(DeleteView):
    model = Article
    template_name = 'news/detail_view.html'
    context_object_name = 'article'
 

def news_detail(request, pk):
    form = CommentForm()
    news = get_object_or_404(Article, id=pk)
    comments = Comment.objects.filter(post=pk)

    if request.method == 'POST':
        f = CommentForm(request.POST)
        if f.is_valid():
            comm = f.save(commit=False)
            comm.post = news
            comm.save()
    return render(request, 'news/detail_view.html', {'article': news, 'comments': comments, 'form': form})



'''def new_single(request, pk):
    """Вывод полной статьи
    """
    new = get_object_or_404(Article, id=pk)
    comment = Comment.objects.filter(new=pk, moderation=True)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.new = new
            form.save()
            return redirect(new_single, pk)
    else:
        form = CommentForm()
    return render(request, "news/new_single.html",
                  {"new": new,
                   "comments": comment,
                   "form": form})'''