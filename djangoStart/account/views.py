from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def liked(request):

    return render(request, 'main/about.html')