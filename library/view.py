from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail

def index(request):
    return render(request, 'index/index.html')


def login(request):
    return render(request, 'admin/admin-login.html')


def welcome(request):
    return render(request, 'index/welcome.html')


def adminadd(request):
    return render(request, 'admin/admin-add.html')


def adminlist(request):
    return render(request, 'admin/admin-list.html')


def send(request):
    send_mail(subject='催还消息', message='你的图书借阅时间快到了，请立即归还图书，否则将会进入黑名单，以后无法借阅', from_email='83521274@qq.com',
              recipient_list=[request.GET['q']], fail_silently=False)
    return HttpResponse('OK')
