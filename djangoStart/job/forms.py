from .models import Comment_job
from django.forms import ModelForm, Textarea, TextInput, IntegerField, Form


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
class JobFilterForm(Form):
    min_price=IntegerField(label="от", required=False)
    max_price=IntegerField(label="до", required=False)