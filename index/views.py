from django.http import HttpResponse
from django.shortcuts import render
from .models import *


def index(request):
    return render(request, 'index/index.html')


def register(request):
    return HttpResponse('Index Register OK')


def change(request):
    return HttpResponse('修改密码')


def login(request):
    return render(request, 'index/user/login.html')


def logout(request):
    return render(request, 'index/user/login.html')


def welcome(request):
    return render(request, 'index/home/welcome.html')


def user_add(request):
    if request.method == 'GET':
        return render(request, 'index/user/add.html')
    else:
        pass


def user_list(request):
    if request.method == 'GET':
        return render(request, 'index/user/list.html')
    else:
        pass


def user_change(request):
    if request.method == 'GET':
        return render(request, 'index/user/add.html')
    else:
        pass


def user_delete(request):
    if request.method == 'GET':
        return render(request, 'index/user/add.html')
    else:
        pass


def product_cate(request):
    return render(request, 'index/product/list.html')


def product_add(request):
    if request.method == 'GET':
        return render(request, 'index/product/add.html')
    else:
        pass


def product_list(request):
    if request.method == 'GET':
        return render(request, 'index/product/list.html')
    else:
        pass


def product_change(request):
    if request.method == 'GET':
        return render(request, 'index/product/add.html')
    else:
        pass


def product_delete(request):
    if request.method == 'GET':
        return render(request, 'index/product/add.html')
    else:
        pass


def event_add(request):
    return render(request, 'index/event/add.html')


def event_work(request):
    return render(request, 'index/event/work.html')


def event_activity(request):
    return render(request, 'index/event/activity.html')


def system_sms(request):
    return render(request, 'index/system/sms.html')


def system_mail(request):
    return render(request, 'index/system/mail.html')


def system_feed(request):
    return render(request, 'index/system/feed.html')


def system_update(request):
    return render(request, 'index/system/update.html')

