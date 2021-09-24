from django import forms
from django.forms import fields
from .models import Question

# class BoardForm(forms.Form):
#     REGION_A = 'sl'
#     REGION_B = 'dj'
#     REGION_C = 'bs'
#     REGION_CHOICES = [
#         (REGION_A, '서울'),
#         (REGION_B, '대전'),
#         (REGION_C, '부산'),
#     ]


#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)
#     region = forms.ChoiceField(choices=REGION_CHOICES, widget=forms.Select())
    
class BoardForm(forms.ModelForm):
    title = forms.CharField(
        label="제목",
        widget=forms.TextInput(
            attrs={
                'class': 'my-title',
                'placeholder': 'Enter the title',
            }
        ),
    )
    category = forms.CharField(
        label="카테고리",
        widget=forms.TextInput(
            attrs={
                'class': 'my-category',
                'placeholder': 'Enter the category',
            }
        )
    )

    content = forms.CharField(
        label="내용",
        widget=forms.Textarea(
            attrs={
                'class': 'my-content',
                'placeholder': 'Enter the content',
                'rows':5,
                'cols':50,
            }
        ),
        error_messages={
            'required': 'Please enter your content'
        }
    )
    
    
    class Meta:
        model = Question
        fields = '__all__'