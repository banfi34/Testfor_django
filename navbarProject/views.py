import os

from django.shortcuts import render, redirect
from django.http import HttpResponse
from os.path import isfile
from django.template.loader import get_template

from .models import Pages
from django.contrib import messages


# Create your views here.


def base_html(request):
    if request.user.is_staff and Pages.objects.all().filter(id=request.user.id):
        pages_list = Pages.objects.all().order_by('id')
        return render(request, 'homes/home.html',
                      {'pages_list': pages_list,
                       })

    elif request.user.is_authenticated and Pages.objects.filter(auth_users__id=request.user.id):
        pages_list = Pages.objects.all().filter(auth_users__id=request.user.id).order_by('id')
        return render(request, 'homes/home.html',
                      {'pages_list': pages_list,
                       })

    else:
        return render(request, 'homes/welcome.html')


def home_html(request, page_name):
    page = Pages.objects.get(page_name=page_name)
    css_path = page_name + '.css'
    template_name = 'templates/navbars/' + page_name + '/' + page_name + '.html'
    base_path = 'navbars/' + page_name + '/' + page_name + '.html'
    template_path = os.path.dirname(template_name)

    if not os.path.exists(template_path):
        os.makedirs(template_path)

    if not isfile(template_name):
        with open('templates/navbars/navbar.html', 'r') as source:
            source_html = source.read()
        with open(template_name, 'w') as destination:
            destination.write(source_html)

    if request.user.is_staff:
        pages_list = Pages.objects.all().order_by('id')
        return render(request, 'homes/home.html',
                      {'pages_list': pages_list,
                       'page_name': page_name,
                       'base_path': base_path,
                       'css_path': css_path,
                       })

    elif request.user.is_authenticated and page.auth_users.filter(id=request.user.id):
        pages_list = Pages.objects.all().filter(auth_users__id=request.user.id).order_by('id')
        return render(request, 'homes/home.html',
                      {'pages_list': pages_list,
                       'page_name': page_name,
                       'base_path': base_path,
                       'css_path': css_path,
                       })

    else:
        messages.add_message(request, messages.INFO,
                             'You dont have access to this site')
        return redirect('home')
