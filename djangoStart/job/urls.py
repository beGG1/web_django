from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.job_home, name='job_home'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='job_detail')
]
