from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name="register"),
    path('login', views.loginpage, name="loginpage"),
    path('home', views.home, name="home"),
    path('adminpage', views.adminpage, name="adminpage"),
    path('doctor', views.doctor, name="doctor"),
    path('patient', views.patient, name="patient"),
]
