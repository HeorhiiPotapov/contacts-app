from django.urls import path
from .views import SignUpView, ActivationView
from django.contrib.auth import views as auth_views

app_name = 'users'
urlpatterns = [
    path('new/', SignUpView.as_view(), name='new'),
    path('login/', auth_views.LoginView.as_view(
        template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='users/logout.html'), name="logout"),
    path('activate/<uidb64>/<token>/',
         ActivationView.as_view(), name='activate')
]
