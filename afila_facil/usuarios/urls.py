from django.urls import path
from django.contrib.auth import views

urlpatterns = [
    path('', views.LoginView.as_view(template_name="usuarios/login.html"), name='login'),
]
