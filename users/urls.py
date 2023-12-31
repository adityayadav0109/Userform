
from django.urls import path
from users import views

urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('user_data/', views.user_data, name="user_data"),
]
