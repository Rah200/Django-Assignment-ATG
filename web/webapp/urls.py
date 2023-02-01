from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login', views.loginpage, name="loginpage"),
    path('logout', views.logout, name="logout"),
    path('register/', views.register, name="register"),
    path('view', views.view, name="view"),
    path('adminpage', views.adminpage, name="adminpage"),
    path('doctor', views.doctor, name="doctor"),
    path('patient', views.patient, name="patient"),
    path('blogpage', views.blogpage, name="blogpage"),
    path('delete_data/<str:pk>', views.delete_data, name="delete_data"),
]
