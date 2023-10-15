from django import forms

from blog.models import Post


class CreatePostForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(), required=False)
    description = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Write something...',
    }))

    class Meta:
        model = Post
        fields = ('image', 'description')

