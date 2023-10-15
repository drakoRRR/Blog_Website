from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms

from blog.models import Comment
from users.models import User

from .tasks import send_email_verification

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput())
    last_name = forms.CharField(widget=forms.TextInput())
    username = forms.CharField(widget=forms.TextInput())
    email = forms.CharField(widget=forms.EmailInput())
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=True)
        send_email_verification.delay(user.id)
        return user

class CommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'comment-input',
        'placeholder': 'Write a comment...',
    }))

    class Meta:
        model = Comment
        fields = ('text',)


class ProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput())
    last_name = forms.CharField(widget=forms.TextInput())
    image = forms.ImageField(widget=forms.FileInput(), required=False)
    username = forms.CharField(widget=forms.TextInput(attrs={
        'readonly': True,
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'readonly': True,
    }))
    description = forms.CharField(widget=forms.TextInput())

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'image', 'username', 'email', 'description')
