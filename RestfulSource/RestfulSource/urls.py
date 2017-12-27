"""RestfulSource URL Configuration

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
from django.conf.urls import url

from api import views


urlpatterns = [
    # url(r'admin/', admin.site.urls),
    # 手动档，手动写这么些个url， name参数可不带
    # url(r'(?P<version>\w+)/users/$', views.UserIndex.as_view(), name='xx'),
    # url(r'(?P<version>\w+)/users\.(?P<format>\w+)/$', views.UserIndex.as_view(), name='xx'),
    # url(r'(?P<version>\w+)/users/(?P<pk>\d+)/$', views.UserIndex.as_view(), name='xxa'),
    # url(r'(?P<version>\w+)/users\.(?P<format>\w+)/(?P<pk>\d+)/$', views.UserIndex.as_view(), name='xx'),
    # 半自动
    # url(r'(?P<version>\w+)/users/$', views.UserIndex.as_view({'get': 'list', 'post': 'create'}), name='xx'),
    # url(r'(?P<version>\w+)/users/(?P<pk>\d+)/$', views.UserIndex.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='xxa'),

    # 自动挡
    # url(r'^(?P<version>\w+)/', include(route.urls))

    # 渲染
    url(r'(?P<version>\w+)/users/$', views.UserIndex.as_view(), name='xx'),
    url(r'(?P<version>\w+)/users\.(?P<format>[a-z0-9]+)', views.UserIndex.as_view(), name='xxx'),
]
