from .models import Comment_job
from django.forms import ModelForm, Textarea, TextInput
from django import forms
from django.core.validators import  MinValueValidator


class JobFilterForm(forms.Form):
    min_price=forms.IntegerField(label="от", required=False, validators=[MinValueValidator(0)])
    max_price=forms.IntegerField(label="до", required=False, validators=[MinValueValidator(0)])

class JobFilterFormFind(forms.Form):
    find=forms.CharField(label="", required=False)


class JobFilterFormGr(forms.Form):
    gr_gib=forms.BooleanField(label="Гибкий", required=False)
    gr_52=forms.BooleanField(label="_5/2", required=False)
    gr_22=forms.BooleanField(label="_2/2", required=False)

class JobFilterFormZan(forms.Form):
    full=forms.BooleanField(label="Полная", required=False)
    notfull=forms.BooleanField(label="_Неполная", required=False)

class CommentForm(ModelForm):
    class Meta:
        model = Comment_job
        fields = ('name', 'email', 'body')

        widgets = {

            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя',
                'style': 'width: 40vw;'
        }),

            "body": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Комментарий',
                'style': 'height:15vh; margin-top:1vw;  width: 40vw;'
            })
        }