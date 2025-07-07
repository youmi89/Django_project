# blog/forms.py

from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    title = forms.CharField(
        max_length=200,
        label='제목',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 10})
    )
    
    class Meta:
        model = Post
        fields = ['title', 'content']