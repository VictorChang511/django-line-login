from django.urls import path
from . import views

urlpatterns = [
  path("", views.index, name="index"),
  path('login', views.login, name='login'),
  path('auth/line/callback', views.callback),
  path('user', views.get_user),
  path('logout', views.logout)
]