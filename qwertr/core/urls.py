from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^accounts/login/$', views.LoginView.as_view(), name="login"),
    url(r'^$', views.HomeView.as_view()),

]
