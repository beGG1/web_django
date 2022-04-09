from .models import Comment
from django.forms import ModelForm, Textarea, TextInput


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

            "email": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'email'
            }),
            "body": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Комментарий',
                'style': 'height:90px; margin-top:1%;  width: 70%;'
            })
        }