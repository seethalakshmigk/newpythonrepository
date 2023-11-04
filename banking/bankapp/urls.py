# urls.py
from django.urls import path
from . import views

app_name = 'bankapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('apply/', views.apply, name='apply'),
    path('app_success/',views.success,name='msg'),
    path('logout/', views.user_logout, name='logout'),
]

