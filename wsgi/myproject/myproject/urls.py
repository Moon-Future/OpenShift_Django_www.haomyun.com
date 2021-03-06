"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
# from PhoneBook.views import index as views_index

urlpatterns = [

    url(r'^admin/', admin.site.urls),

    url(r'^$', 'PhoneBook.views.index',name='index'),
    url(r'^phonenum$', 'PhoneBook.views.phone',name='phonenum'),
    url(r'^(?P<pk>\d+)/$', 'PhoneBook.views.phone',name='phonenum'),
    url(r'^add/$', 'PhoneBook.views.add',name='add'),
    url(r'^delete/$', 'PhoneBook.views.delete',name='delete'),
    url(r'^(?P<pk>\d+)/detail/$', 'PhoneBook.views.detail',name='datail'),
    url(r'^login/$', 'PhoneBook.views.login',name='login'),
    url(r'^jianli/$', 'PhoneBook.views.jianli',name='jianli'),
]
