from django.shortcuts import render
from job.models import Job
from news.models import Article


def index(request):
    data = {
        'title': 'Главная страница'
    }
    news = Article.objects.all()[:5]
    jobs = Job.objects.all()[:5]
    return render(request, 'main/index.html', {'news': news, 'jobs':jobs})

def about(request):
    return render(request, 'main/about.html')


def contact(request):
    return render(request, 'main/contact.html')
