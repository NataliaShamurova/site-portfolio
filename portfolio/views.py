from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from config.settings import EMAIL_HOST_USER
from portfolio.models import Author, Project, Contact
from .forms import ContactForm

menu = [
    {'title': "Главная", 'url_name': 'home'},
    {'title': "Проекты", 'url_name': 'project'},
    {'title': "Резюме", 'url_name': 'about'},
    {'title': "Контакты", 'url_name': 'contact'},
]


def home(request):
    author = Author.objects.first()
    data = {
        'title': 'Home',
        'menu': menu,
        'author': author
    }
    return render(request, 'portfolio/home.html', context=data)


def about(request):
    author = Author.objects.first()
    data = {
        'title': 'Обо мне',
        'content': 'Резюме',
        'menu': menu,  # Меню для отображения
        'author': author
    }
    return render(request, 'portfolio/about.html', context=data)


def project(request):
    author = Author.objects.first()
    projects = Project.objects.all()
    context = {
        'title': 'Проекты',
        'menu': menu,  # Меню для отображения
        'projects': projects,
        'author': author,
    }
    return render(request, 'portfolio/project.html', context=context)


def project_detail(request, slug):
    projects = get_object_or_404(Project, slug=slug)
    author = Author.objects.first()
    stack_list = [item.strip() for item in projects.stack.split(".")]

    context = {
        'title': 'О проекте',
        'menu': menu,
        'projects': projects,
        'author': author,
        'stack_list': stack_list,
    }
    return render(request, 'portfolio/project_detail.html', context)


def contact(request):
    author = Author.objects.first()
    sites = Contact.objects.all()
    context = {
        'title': 'Контакты',
        'menu': menu,
        'author': author,
        'sites': sites,
    }

    form = ContactForm()  # Инициализация формы по умолчанию

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Отправка почты
            send_mail(
                f'Сообщение от {name} <{email}>',
                message,
                EMAIL_HOST_USER,  # email для отправки
                [EMAIL_HOST_USER],  # email для получения сообщений
                fail_silently=False,
            )
            context['success'] = True  # Сообщение об успешной отправке

    context['form'] = form  # Передаем форму, включает ошибки, если есть

    return render(request, 'portfolio/contact.html', context)
