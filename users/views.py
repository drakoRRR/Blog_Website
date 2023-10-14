from django.contrib import auth, messages
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from users.forms import UserLoginForm, UserRegisterForm
from users.models import User, EmailVerification


# Create your views here.
class LoginUserView(LoginView):
    template_name = 'users/login_page.html'
    form_class = UserLoginForm

    def form_invalid(self, form):
        messages.error(self.request, 'There was an error with username or password, check again !')
        return super().form_invalid(form)


class RegistrationView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register_page.html'
    success_url = reverse_lazy('blog:feed')

    def form_valid(self, form):
        response = super().form_valid(form)
        auth.login(self.request, self.object, backend='django.contrib.auth.backends.ModelBackend')
        return response

    def form_invalid(self, form):
        messages.error(self.request, 'There was an error with username or password, check again !')
        return super().form_invalid(form)


class EmailVerificationView(TemplateView):
    template_name = 'users/email_success_page.html'

    def get(self, request, *args, **kwargs):
        code = kwargs['code']
        user = User.objects.get(email=kwargs['email'])
        email_verification = EmailVerification.objects.filter(user=user, code=code)

        if email_verification.exists() and not email_verification.first().is_expired():
            user.is_verified_email = True
            user.save()
            return super(EmailVerificationView, self).get(request, *args, **kwargs)
        else:
            return redirect('blog:feed')
