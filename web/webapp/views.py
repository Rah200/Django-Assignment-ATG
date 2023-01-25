from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout


def home(request):
    return render(request, 'home.html')


def loginpage(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('admin')
            elif user is not None and user.is_doctor:
                login(request, user)
                return redirect('doctor')
            elif user is not None and user.is_patient:
                login(request, user)
                return redirect('patient')
            else:
                msg = 'Invalid username or password'
        else:
            msg = 'Validation Failed...'
    return render(request, 'login.html', {'form': form, 'msg': msg})


def register(request):
    msg = None
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'Registration successful'
            return redirect('loginpage')
        else:
            msg = 'Registration failed'
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form, 'msg': msg})


def adminpage(request):
    return render(request, 'admin.html')


def doctor(request):
    return render(request, 'doctor.html')


def patient(request):
    return render(request, 'patient.html')
