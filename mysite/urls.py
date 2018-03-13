"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.contrib import admin
from . import get
import polls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('get/', get.get),
    path('list/', get.list),
    path('shaixuan/', get.getButton),
    path('index/', get.getIndex),
    path('dingdan/', get.dingdan),
    path('gwc/', get.gwc),
    path('sjd_list', get.sjd_get),
    path('sjd_remove', get.sjd_remove),
    path('sjd_add_cloth', get.sjd_add_cloth),
    path('get_all_cloth', get.get_all_cloth),
    path('create_sjd', get.create_sjd),
    path('save_sjd', get.save_sjd),
    path('del_sjd', get.del_sjd),
    url(r'^polls/', include('polls.urls')),
]
