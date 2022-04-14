from .models import Comment_job
from django.forms import ModelForm, Textarea, TextInput
from django import forms
from django.core.validators import  MinValueValidator


class JobFilterForm(forms.Form):
    min_price=forms.IntegerField(label="от", required=False, validators=[MinValueValidator(0)])
    max_price=forms.IntegerField(label="до", required=False, validators=[MinValueValidator(0)])

class JobFilterFormFind(forms.Form):
    find=forms.CharField(label="Название или специальность", required=False)


class JobFilterFormGr(forms.Form):
    gr_gib=forms.BooleanField(label="Гибкий", required=False)
    gr_52=forms.BooleanField(label="5/2", required=False)
    gr_22=forms.BooleanField(label="2/2", required=False)

class JobFilterFormZan(forms.Form):
    full=forms.BooleanField(label="Полная", required=False)
    notfull=forms.BooleanField(label="Неполная", required=False)

class CommentForm(ModelForm):
    class Meta:
        model = Comment_job
        fields = ('name', 'email', 'body')

        widgets = {

            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя',
                'style': 'width: 600px;'
        }),

            "body": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Комментарий',
                'style': 'height:90px; margin-top:1%;  width: 600px;'
            })
        }