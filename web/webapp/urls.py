from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.register, name="register"),
    path('login', views.loginpage, name="loginpage"),
    path('home', views.home, name="home"),
    path('adminpage', views.adminpage, name="adminpage"),
    path('doctor', views.doctor, name="doctor"),
    path('patient', views.patient, name="patient"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
