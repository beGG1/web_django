from django.shortcuts import render
from django.views.generic import DeleteView
from .models import Job

# Create your views here.
def job_home(request):
    jobs = Job.objects.all()
    return render(request, 'job/job_home.html', {'jobs': jobs})


class NewsDetailView(DeleteView):
    model = Job
    template_name = 'job/detail_view.html'
    context_object_name = 'job'