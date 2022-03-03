from django.shortcuts import render
from django.views.generic import DeleteView
from .models import Article

# Create your views here.
def news_home(request):
    news = Article.objects.all()
    return render(request, 'news/news_home.html', {'news': news})


class NewsDetailView(DeleteView):
    model = Article
    template_name = 'news/detail_view.html'
    context_object_name = 'article'