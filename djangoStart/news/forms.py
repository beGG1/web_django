from tkinter.ttk import Style
from .models import Comment
from django.forms import ModelForm, Textarea, TextInput
from account.models import Liked_post
from django import forms

class ArticleFilterForm(forms.Form):
    find=forms.CharField(label="", required=False)


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

        widgets = {

            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя',
                'style': 'width: 70%;'
        }),

            "body": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Комментарий',
                'style': 'height:90px; margin-top:1%;  width: 70%;'
            })
        }

