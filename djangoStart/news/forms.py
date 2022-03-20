from .models import Comment
from django.forms import ModelForm, Textarea, TextInput


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

        widgets = {

            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
        }),

            "email": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'email'
            }),
            "body": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'text'
            })
        }