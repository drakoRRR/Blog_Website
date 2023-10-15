from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import LoginUserView, RegistrationView, EmailVerificationView, ProfileView

app_name = 'users'

urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('verify/<str:email>/<uuid:code>/', EmailVerificationView.as_view(), name='email_verification'),

    path('profile/<int:user_id>/', ProfileView.as_view(), name='profile'),
    path('profile/<int:user_id>/<int:post_id>', ProfileView.as_view(), name='profile_with_post'),
]
