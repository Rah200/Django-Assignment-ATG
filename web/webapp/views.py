from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm, BlogForm
from django.contrib.auth import authenticate, login, logout
from .models import User, Blog
from django.views import View


def home(request):
    form = Blog.objects.all()
    context = {'form': form}
    return render(request, 'home.html', context)


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
                return redirect('home')
            elif user is not None and user.is_doctor:
                login(request, user)
                return redirect('home')
            elif user is not None and user.is_patient:
                login(request, user)
                return redirect('home')
            else:
                msg = 'Invalid username or password'
        else:
            msg = 'Validation Failed...'
    return render(request, 'login.html', {'form': form, 'msg': msg})


def register(request):
    msg = None
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            msg = 'Registration successful'
            return redirect('loginpage')
        else:
            msg = 'Registration failed'
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form, 'msg': msg})


def blogpage(request):
    form = BlogForm
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'blogpage.html', context)


def delete_data(request, pk):
    blog_data = Blog.objects.get(id=pk)
    blog_data.delete()
    return redirect('home')


def view(request):
    form = Blog.objects.all()
    context = {'form': form}
    return render(request, 'view.html', context)


def logout(request):
    if request.method == 'POST':
        logout(request)
    return render(request, 'login.html')


def adminpage(request):
    return render(request, 'adminpage.html')


def doctor(request):
    return render(request, 'doctor.html')


def patient(request):
    return render(request, 'patient.html')
