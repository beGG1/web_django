from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Liked_post, Liked_job
# Create your views here.

@login_required
def liked(request):
    like_a = Liked_post.objects.filter(id_user=request.user)
    like_j = Liked_job.objects.filter(id_user=request.user)
    return render(request, 'account/home.html', {'article': like_a, 'job': like_j})