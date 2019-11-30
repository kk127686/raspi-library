from django.urls import path

from . import views

app_name = 'index'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('change/', views.change, name='change'),
    path('welcome/', views.welcome, name='welcome'),


    path('user/add/', views.user_add,name='user_add'),
    path('user/list/', views.user_list, name='user_list'),
    path('user/change/', views.user_change, name='user_change'),
    path('user/delete/', views.user_delete, name='user_delete'),

    path('product/cate/', views.product_cate, name='product_cate'),
    path('product/add/', views.product_add, name='product_add'),
    path('product/list/', views.product_list, name='product_list'),
    path('product/change/', views.product_change, name='product_change'),
    path('product/delete/', views.product_delete, name='product_delete'),

    path('event/add/', views.event_add, name='event_add'),
    path('event/work/', views.event_work, name='event_work'),
    path('event/activity/', views.event_activity, name='event_activity'),

    path('system/feed', views.system_feed, name='system_feed'),
    path('system/update', views.system_update, name='system_update'),
    path('system/sms', views.system_sms, name='system_sms'),
    path('system/mail', views.system_mail, name='system_mail'),
]