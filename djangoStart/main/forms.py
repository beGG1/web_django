from django import forms
from job.models import Job
from news.models import Article
from django.forms import ModelForm, Textarea, TextInput

class Find(forms.Form):
    find=forms.CharField(label="", required=False)

