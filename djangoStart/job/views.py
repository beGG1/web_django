from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DeleteView
from .models import Job, Comment_job
from .forms import CommentForm
from account.models import Liked_job

# Create your views here.
def job_home(request):
    jobs = Job.objects.all()
    return render(request, 'job/job_home.html', {'jobs': jobs})


class NewsDetailView(DeleteView):
    model = Job
    template_name = 'job/detail_view.html'
    context_object_name = 'job'


def job_detail(request, pk):
    form = CommentForm()
    job = get_object_or_404(Job, id=pk)
    comments = Comment_job.objects.filter(post=pk)

    if request.method == 'POST':
        f = CommentForm(request.POST)
        if f.is_valid():
            comm = f.save(commit=False)
            comm.post = job
            comm.save()
    return render(request, 'job/detail_view.html', {'job': job, 'comments': comments, 'form': form})


def like(request, pk):
    print('like')
    job = get_object_or_404(Job, id=pk)
    print(Liked_job(id_user=request.user, id_job=job))
    if Liked_job(id_user=request.user, id_job=job) is not None:
        print('jopa')
        l = Liked_job(id_user=request.user, id_job=job)
        l.save()
    
    return redirect('home')

def unlike(request, pk):
    job = get_object_or_404(Job, id=pk)
    
    Liked_job.objects.filter(id_user=request.user, id_job=job).delete()
    
    return redirect('home')