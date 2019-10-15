from django.shortcuts import render

def index(request):
    return render(request,'index/index.html')
def login(request):
    return  render(request, '/admin/admin-login.html')
def welcome(request):
    return  render(request,'index/welcome.html')
def adminadd(request):
    return  render(request,'admin/admin-add.html')
def adminlist(request):
    return render(request,'admin/admin-list.html')