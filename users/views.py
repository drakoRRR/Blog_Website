from django.contrib import auth, messages
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import UserLoginForm, UserRegisterForm
from users.models import User


# Create your views here.
class LoginUserView(LoginView):
    template_name = ''
    form_class = UserLoginForm

    def form_invalid(self, form):
        messages.error(self.request, 'There was an error with username or password, check again !')
        return super().form_invalid(form)


class RegistrationView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = ''
    success_url = reverse_lazy('products:landing')

    def form_valid(self, form):
        response = super().form_valid(form)
        auth.login(self.request, self.object, backend='django.contrib.auth.backends.ModelBackend')
        return response

    def form_invalid(self, form):
        messages.error(self.request, 'There was an error with username or password, check again !')
        return super().form_invalid(form)
