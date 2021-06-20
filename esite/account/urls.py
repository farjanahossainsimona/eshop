from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='account.index'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
]
