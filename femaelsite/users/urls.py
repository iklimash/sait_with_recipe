from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView

app_name = 'users'


urlpatterns = [

    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('password-change/', views.UserPasswordChange.as_view(), name='password_change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(template_name = 'users/password_change_done.html'), name='password_change_done'),
    path('register/', views.register, name='register'),

]
