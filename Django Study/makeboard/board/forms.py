from django import forms
from django.forms import fields
from .models import Question

class BoardForm(forms.ModelForm):
    title = forms.CharField(
        label="제목",
        widget=forms.TextInput(
            attrs={
                'class':'my-title',
                'placeholder': 'Enter the title',
            }
        )
    )

    category = forms.CharField(
        label="카테고리",
        widget=forms.TextInput(
            attrs={
                'class':'my-category',
                'placeholder': 'Enter the category',
            }
        )
    )

    content = forms.CharField(
        label="내용",
        widget=forms.Textarea(
            attrs={
                'class':'my-content',
                'placeholder':'Enter the content'
            }
        )
    )

    class Meta:
        model = Question
        fields = '__all__'