from django import forms
from django.contrib.auth.forms import UserChangeForm

from blog.models import Post


class CreatePostForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(), required=False)
    description = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Write something...',
    }))

    class Meta:
        model = Post
        fields = ('image', 'description')


class UpdatePostForm(UserChangeForm):
    image = forms.ImageField(widget=forms.FileInput(), required=False)
    description = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Update your post...',
    }))

    class Meta:
        model = Post
        fields = ('image', 'description')

