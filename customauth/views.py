from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from Finance.forms import (
    UserLoginForm,
)


class UserLogin(LoginView):
    authentication_form = UserLoginForm
    template_name = 'Finance/login.html'
    redirect_authenticated_user = True
    next_page = '/'


class UserLogout(LogoutView):
    next_page = '/login/'


class PasswordChangeView(PasswordChangeView):
    pass


class PasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'Finance/template_replace.html'
    next_page = '/'


