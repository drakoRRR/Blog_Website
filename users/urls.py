from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import LoginUserView, RegistrationView, EmailVerificationView, ProfileView, SettingsView, send_request, \
    accept_request, FriendsView

app_name = 'users'

urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('verify/<str:email>/<uuid:code>/', EmailVerificationView.as_view(), name='email_verification'),

    path('profile/<int:user_id>/', ProfileView.as_view(), name='profile'),
    path('profile/<int:user_id>/<int:post_id>', ProfileView.as_view(), name='profile_with_post'),

    path('profile/settings/<int:pk>', SettingsView.as_view(), name='settings'),

    path('add-friend/<int:id>/', send_request, name='add_friend'),
    path('accept/<int:id>/', accept_request, name='accept_friend'),
    path('friends/<int:pk>', FriendsView.as_view(), name='friends'),
]
