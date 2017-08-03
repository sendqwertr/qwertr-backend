from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from . import forms


class LoginView(auth_views.LoginView):
    form_class = forms.AuthenticateForm


class HomeView(TemplateView):
    template = 'home.html'
