# task_manager/views.py
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from .forms import UserRegistrationForm, UserLoginForm

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm
from django.core.paginator import Paginator


@login_required  # Эта линия гарантирует, что только аутентифицированные пользователи получат доступ к данному методу
def home(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()  # Сохранение новой задачи
            return redirect('home')  # Переход на ту же страницу или на другую

    else:
        form = TaskForm()

    tasks = Task.objects.all()  # Получение всех задач
    return render(request, 'task_manager/home.html', {'tasks': tasks, 'form': form})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm()
    tasks = Task.objects.filter(parent_task__isnull=True)

    return render(request, 'task_manager/add_task.html', {'form': form,  'tasks': tasks})


def edit_task(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_manager/task_form.html', {'form': form})

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('home')

def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()
    return redirect('home')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Устанавливаем зашифрованный пароль
            user.save()
            return redirect('login')  # Перенаправляем на страницу логина
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'task_manager/registration/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')  # Перенаправляем на страницу входа


from django.core.paginator import Paginator


def task_list(request):
    tasks = Task.objects.all()

    # Фильтрация
    priority_filter = request.GET.get('priority')
    if priority_filter:
        tasks = tasks.filter(priority=priority_filter)

    # Сортировка
    sort_by = request.GET.get('sort_by', 'created_at')
    tasks = tasks.order_by(sort_by)

    paginator = Paginator(tasks, 10)  # 10 задач на страницу
    page_number = request.GET.get('page')
    tasks_paginated = paginator.get_page(page_number)

    return render(request, 'task_manager/add_task.html', {'tasks': tasks_paginated})