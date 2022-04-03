from re import template
from django.shortcuts import redirect, render
from job.models import Job
from news.models import Article
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout


def index(request):
    data = {
        'title': 'Главная страница'
    }
    news = Article.objects.all()[:5]
    jobs = Job.objects.all()[:5]
    return render(request, 'main/index.html', {'news': news, 'jobs':jobs})

def about(request):
    return render(request, 'main/about.html')


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')


def logout_user(request):
    logout(request)
    return redirect('login')

class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'main/login.html'
    
    def get_success_url(self):
        return reverse_lazy('home')
